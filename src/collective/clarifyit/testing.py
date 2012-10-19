from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

import collective.clarifyit


COLLECTIVE_CLARIFYIT = PloneWithPackageLayer(
    zcml_package=collective.clarifyit,
    zcml_filename='testing.zcml',
    gs_profile_id='collective.clarifyit:testing',
    name="COLLECTIVE_CLARIFYIT")

COLLECTIVE_CLARIFYIT_INTEGRATION = IntegrationTesting(
    bases=(COLLECTIVE_CLARIFYIT, ),
    name="COLLECTIVE_CLARIFYIT_INTEGRATION")

COLLECTIVE_CLARIFYIT_FUNCTIONAL = FunctionalTesting(
    bases=(COLLECTIVE_CLARIFYIT, ),
    name="COLLECTIVE_CLARIFYIT_FUNCTIONAL")
