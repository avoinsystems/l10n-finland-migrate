from openerp.osv import osv, fields
from openerp.tools.translate import _

    
class Partner(osv.Model):      

    _inherit = "res.partner"
    _name = "res.partner"
    
    def onchange_industry_industry(self, cr, uid, ids, industry, context=None):
        industry = self.pool.get('business_industry.industry').browse(cr, uid, industry, context=context)
        
        val = { 'business_industry_category': industry.category }
        
        return {'value': val}
    
    def onchange_industry_category(self, cr, uid, ids, industry_category, context):
        cat = self.pool.get('business_industry.category').browse(cr, uid, industry_category, context=context)
        
        val = { 'business_industry_class': cat.industry_class }
        
        return {'value': val}
    
    _columns = {
        'business_industry_class':  fields.many2one('business_industry.class', string='Industry class'),
        'business_industry_category':  fields.many2one('business_industry.category', string='Industry category'),
        'business_industry_industry':  fields.many2one('business_industry.industry', string='Business industry'),
    }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
