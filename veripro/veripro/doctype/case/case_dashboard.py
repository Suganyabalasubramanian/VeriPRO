from __future__ import unicode_literals
import frappe
from frappe import _
def get_data():
    return {
        'heatmap': True,
        'heatmap_message': _('This is based on the Time Sheets created against this project'),
        'fieldname': 'case_id',
        'transactions': [
            {
                'label': _('Checks'),
                'items': ['Address Check','Education Check','Employment','Test','Identity Check','Criminal Check','Medical Check']
            },
            {
                'label': _('Verify Checks'),
                'items': ['Verify Address Check','Verify Education Check','Verify Employment','Verify Test','Verify Identity Check','Verify Criminal Check','Verify Medical Check']
            }
            
        ]
    }
