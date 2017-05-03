# -*- coding: utf-8 -*-

# 1. Standard library imports:
import re

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models
from openerp.exceptions import ValidationError
from openerp import _

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ResPartner(models.Model):
    
    # 1. Private attributes
    _inherit = 'res.partner'

    # 2. Fields declaration
    business_id = fields.Char('Business id')

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges
    @api.onchange('business_id')
    def onchange_business_id_update_format(self):
        # Reformat business id from 12345671 to 1234567-1
        if isinstance(self.business_id, basestring) and re.match('^[0-9]{8}$', self.business_id):
            self.business_id = self.business_id[:7] + '-' + self.business_id[7:]

    @api.constrains('business_id')
    def _validate_business_id(self):
        # Business id can be empty
        if not self.business_id:
            return True

        # Validate format etc.
        if self.country_id and self.country_id.code:
            country_code = self.country_id.code
            method_name = "action_validate_business_id_" + country_code.lower()

            # Run country-specific validators
            if hasattr(self, method_name):
                getattr(self, method_name)()

            # TODO: else: generic validator (format, characters)

        else:
            # No country or country code. We can't validate
            return True

        # We should never get to this point, but if there is no errors, return True
        return True

    # TODO: country aware validator
    def _validate_business_id_format(self, business_id=False):
        business_id = business_id or self.business_id

        # Country code is not FI, skip this
        if hasattr(self, 'country_code') and self.country_id.code != 'FI':
            return True

        business_id = business_id or self.business_id

        # Business id is not set. This is fine.
        if not business_id:
            return True

        # Validate registered association format
        # TODO: validate this
        if re.match('^[0-9]{3}[.][0-9]{3}$', business_id):
            # Registered association(rekisteröity yhdistys, ry / r.y.). Format 123.456
            return True

        # Validate business id formal format
        if re.match('^[0-9]{7}[-][0-9]{1}$', business_id):
            return True

        return False

    # TODO: country aware validator
    def _validate_business_id_validation_number(self, business_id=False):
        business_id = business_id or self.business_id

        multipliers = [7, 9, 10, 5, 8, 4, 2]  # Number-space spesific multipliers
        validation_multiplier = 0  # Initial multiplier
        number_index = 0  # The index of the number we are parsing

        business_id_number = re.sub("[^0-9]", "", business_id)  # business id without "-" for validation
        validation_bit = business_id_number[7:8]

        # Test the validation bit
        for number in business_id_number[0:7]:
            validation_multiplier += multipliers[number_index] * int(number)
            number_index += 1

        modulo = validation_multiplier % 11

        # Get the final modulo
        if 2 <= modulo <= 10:
            modulo = 11 - modulo

        if int(modulo) != int(validation_bit):
            return False

        return True

    # 6. CRUD methods

    # 7. Action methods
    @api.multi
    def action_validate_business_id_fi(self):
        # Validate Finnish business ID
        if self.country_id.code == 'FI':
            if not self._validate_business_id_format():
                msg = _("Your business id '%s' is invalid. Please use format 1234567-1" % self.business_id)
                raise ValidationError(msg)

            # The formal format is ok, check the validation number
            if not self._validate_business_id_validation_number():
                msg = _("Your business id '%s' is invalid. Please check the given business id" % self.business_id)
                raise ValidationError(msg)

    # 8. Business methods
    @api.model
    def _init_business_ids(self):
        # When the module is installed update business ids from alternatively named fields
        partners = self.search([])

        if not partners:
            return False

        if hasattr(partners[0], 'businessid'):
            for partner in partners:
                if partner.businessid:
                    partner.business_id = partner.businessid