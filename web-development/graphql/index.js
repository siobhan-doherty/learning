const express = require("express");
const app = express(); 
import { graphqlHTTP } from "express-graphql";
import schema from "./data/schema";
import resolvers from "./data/resolvers";

app.get("/", (req, res) => {
    res.send("GraphQL is quite lovely!");
});

const root = resolvers;

app.use("/graphql", graphqlHTTP({
    schema: schema, 
    rootValue: root,
    graphiql: true
}));

app.listen(8080, () => console.log("Running server on port localhost:8080/graphql"));