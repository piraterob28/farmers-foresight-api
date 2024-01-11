import strawberry
from strawberry.fastapi import GraphQLRouter
from app.graphql_app.query import Query


schema = strawberry.Schema(Query)
graphql_app = GraphQLRouter(schema)