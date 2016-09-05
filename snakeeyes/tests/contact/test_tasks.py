from snakeeyes.extensions import mail
from snakeeyes.blueprints.api.tasks import deliver_email


class TestTasks(object):
    def test_deliver_support_email(self):
        """ Deliver a contact email. """
        form = {
          'email': 'foo@bar.com',
          'message': 'Test message from Snake Eyes.'
        }

        with mail.record_messages() as outbox:
            deliver_email(form.get('email'))

            assert len(outbox) == 1
            assert form.get('email') in outbox[0].body
