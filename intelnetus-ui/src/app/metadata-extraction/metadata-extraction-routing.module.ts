import { NgModule } from "@angular/core";
import { Route, RouterModule } from "@angular/router";
import { MetadataExtractionComponent } from "./metadata-extraction.component";

const routes: Route[] = [
    {
        path: '',
        component: MetadataExtractionComponent
    }
]

@NgModule({
    imports:  [RouterModule.forChild(routes)],
    exports: [RouterModule]
})

export class MetadataExtractionRoutingModule { } 