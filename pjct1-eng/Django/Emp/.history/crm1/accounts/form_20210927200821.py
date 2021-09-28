# forms.py
from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget

JSignatureField(widget=JSignatureWidget(jsignature_attrs={'color': '#CCC'}))