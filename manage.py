import unittest
from flask.cli import FlaskGroup
from project import create_app, db 
from project.models import Product

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command()
def recreate_db():
    """ drops and recreate db """

    db.drop_all()
    db.create_all()
    db.session.commit()

    
@cli.command()
def seed_db():
    """ Seeds the database """

    seed_data = [
        {
            'title': 'Snowboard',
            'price': 888.88,
            'inventory_count': 5
        },
        {
            'title': 'Helmet',
            'price': 100.00,
            'inventory_count': 0
        },
        {
            'title': 'Boots',
            'price': 120.00,
            'inventory_count': 10
        }
    ]

    for data in seed_data:
        db.session.add(Product(title=data['title'], price=data['price'], inventory_count=data['inventory_count']))
    db.session.commit()


@cli.command()
def test():
    """ Runs the tests without code coverage """

    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    cli()