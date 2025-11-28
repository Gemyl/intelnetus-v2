import { Metadata, NetworkData } from "../models/metadata-extraction.model";
import { Link, Node } from "../models/metadata-network.model"

export function buildNetwork(data: Array<Metadata>): {nodes: Array<Node>, links: Array<Link>} {
    let networkData: NetworkData = {nodes: [], links: []};

    for(let primaryIndex = 0; primaryIndex < data.length; primaryIndex++) {
        // add each author to network's nodes if hasn't been added already
        if(networkData.nodes.find((item) => item.id == data[primaryIndex].authorId) == null) {
            networkData.nodes.push({id: data[primaryIndex].authorId, label: `${data[primaryIndex].authorFirstName} ${data[primaryIndex].authorLastName}`});
        }

        // add each publication as network's link
        for(let secondaryIndex = primaryIndex + 1; secondaryIndex < data.length; secondaryIndex++) {
            if(data[primaryIndex].publicationId == data[secondaryIndex].publicationId && data[primaryIndex].authorId != data[secondaryIndex].authorId) {
                networkData.links.push({id: data[primaryIndex].publicationId, source: data[primaryIndex].authorId, target: data[secondaryIndex].authorId});
            }
        }
    }

    return networkData;
}