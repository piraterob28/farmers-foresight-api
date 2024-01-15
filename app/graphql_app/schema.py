import strawberry
from strawberry.fastapi import GraphQLRouter
from app.graphql_app.query import Query
from app.graphql_app.mutation import Mutation


schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)