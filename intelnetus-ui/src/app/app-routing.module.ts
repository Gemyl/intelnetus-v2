import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MetadataExtractionComponent } from './metadata-extraction/metadata-extraction.component';
import { HomeComponent } from './home/home.component';

const routes: Routes = [
  {path:'', component: HomeComponent},
  {path:'metadata-extraction', component: MetadataExtractionComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
