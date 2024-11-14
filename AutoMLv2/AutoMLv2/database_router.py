class MyDatabaseRouter:
    """
    Un routeur pour gérer les opérations de base de données MongoDB.
    """

    def db_for_read(self, model, **hints):
        # Redirige les lectures vers MongoDB pour les modèles Mongo.
        if model._meta.app_label == 'app_mongo':
            return 'mongo'
        return 'default'

    def db_for_write(self, model, **hints):
        # Redirige les écritures vers MongoDB pour les modèles Mongo.
        if model._meta.app_label == 'app_mongo':
            return 'mongo'
        return 'default'

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # Gère la migration : SQL pour SQL, Mongo pour Mongo.
        if app_label == 'app_mongo':
            return db == 'mongo'
        return db == 'default'