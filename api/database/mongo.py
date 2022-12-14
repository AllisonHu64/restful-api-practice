"""Contains a handler for MongoDB database.

Encapsulates some commonly used MongoDB functionality.
"""

class MongoDBHandler():
    """Handles common Mongo Database operations, such as insert,
    find, modify and delete.

    Attributes:
        _db: A mongo client.
        _logger: A logger.
    """

    def __init__(self, app):
        """Inits MongoDBHandlerClass with app.

        Args:
            app: An application that contains a config.MONGO_HOST 
            attribute.
        """

    
    def insert_one(self, col, document):
        """Inserts new document/row into Mongo Database collection/
        table.

        Args:
            col: Collection/Table name.
            document: Document/Row to be inserted.

        Returns:
            An instance of pymongo.results.InsertOneResult.

        Raise:
            DuplicateDocument: A duplicate document already exists.
        """

    def find(self, col, filter=None):
        """Finds all qualifying documents/rows into Mongo Database 
        collection/table based on the filter.

        Args:
            col: Collection/Table name.
            filter: A query document that selects which documents 
                to include in the result set. Can be an empty document 
                to include all documents.

        Returns:
            An array of documents/rows.
        """

    def update_one(self, col, filter=None, update):
        """Update one row into Mongo Database collection/table based 
        on the filter.

        Args:
            col: Collection/Table name.
            filter: A query document that selects which documents 
                to include in the result set. Can be an empty document 
                to include all documents.
            update: The update operations to apply.

        Returns:
            The updated document/row.
        """
    
    def delete(self, col, filter=None):
        """Delete one row into Mongo Database collection/table based 
        on the filter.

        Args:
            col: Collection/Table name.
            filter: A query document that selects which documents 
                to include in the result set. Can be an empty document 
                to include all documents.

        Returns:
            The deleted document/row.
        """

        

