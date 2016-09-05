from snakeeyes.app import create_celery_app
celery = create_celery_app()


@celery.task()
def deliver_email(email):
    print 'deliver_email'
    print {'email': email}
    return 'deliver-email-return-value'


@celery.task()
def print_hello():
    print 'hello'
    return 'hello-return-value'
