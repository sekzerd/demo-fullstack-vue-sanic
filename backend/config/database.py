from . import app_config


def get_db_url():
    c = app_config.Config()
    if c.load():
        return "mysql://{}:{}@{}:{}/{}".format(
            c.user, c.password, c.mysql_ip, c.mysql_port, c.db
        )
    else:
        return "mysql://user:password@db/db"


# def register_databases(app: Sanic):
#     register_tortoise(
#         app,
#         db_url=get_db_url(),
#         modules={"models": ["models.update_logs"]},
#         generate_schemas=True,
#     )
#     return app
