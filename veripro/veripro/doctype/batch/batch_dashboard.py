from __future__ import unicode_literals
import frappe
from frappe import _
def get_data():
    return {
        'heatmap': True,
        'heatmap_message': _('This is based on the Time Sheets created against this project'),
        'fieldname': 'batch',
        'transactions': [
            {
                'label': _('Checks'),
                'items': ['Address Check','Education Check','Employment','Test','Identity Check']
            },
            {
                'label': _('Case'),
                'items': ['Case']
            }
           
            
        ]
    }
