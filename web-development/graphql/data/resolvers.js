import { reject } from "lodash";
import { Widgets } from "./dbConnectors"; 

export const resolvers = {  
    getProduct: ({ id }) => {
        return Widgets.findOne({ _id: id })
        .then((product) => {
            return product;
        })
        .catch((err) => {
            throw new Error(`Failed to retrieve product: ${err.message}`);
        });
    },
    getAllProducts: () => {
        return Widgets.find({})
    },
    createProduct: ({ input }) => {
        const newWidget = new Widgets({
            name: input.name, 
            description: input.description,
            price: input.price,
            soldout: input.soldout,
            inventory: input.inventory,
            stores: input.stores,
        });

        return newWidget.save()
        .then((savedWidget) => {
            savedWidget.id = savedWidget._id;
            return savedWidget;
        })
        .catch((err) => {
            throw new Error(`Failed to create new widget: ${err.message}`);
        });
    },
    updateProduct: ({ input }) => {
        return Widgets.findByIdAndUpdate({ _id: input.id}, input, { new: true })
        .then((widget) => {
            return widget;
        })
        .catch((err) => {
            throw new Error(`Failed to update widget: ${err.message}`);
        });
    }, 
    deleteProduct: ({ id }) => {
        return Widgets.deleteOne({ _id: id })
        .then(() => {
            return "Successfully deleted widget";
        })
        .catch((err) => {
            throw new Error(`Failed to delete widget: ${err.message}`)
        });
    }    
}; 

export default resolvers;