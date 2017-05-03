from openerp.osv import osv, fields
from openerp.tools.translate import _

class Business_industry(osv.Model):      

    _name = "business_industry.industry"
    _order = "code"
    
    def name_get(self, cr, uid, ids, context=None):
        res = []
        for record in self.browse(cr, uid, ids, context):
            name ='[%s] %s' % (record.code, record.name)
            res.append((record.id, name))
        
        return res
    
    def name_search(self, cr, uid, name, args=None, operator='ilike', context=None, limit=20):
        if not args:
            args = []
        if not context:
            context = {}
        if name:
            ids = self.search(cr, uid, ['|',('name', operator, name),('code', operator, name)] + args, limit=limit, context=context)
        else:
            ids = self.search(cr, uid, args, limit=limit, context=context)
        return self.name_get(cr, uid, ids, context)
    
    _columns = {
        'name': fields.char(string='Industry name', size=512),          
        'code': fields.char(string='Industry code', size=6),          
        'category':  fields.many2one('business_industry.category', string='Industry category'),
    }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
