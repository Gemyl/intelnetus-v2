import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MetadataExtractionComponent } from './metadata-extraction/metadata-extraction.component';
import { HomeComponent } from './home/home.component';

const routes: Routes = [
  {path:'', component: HomeComponent},
  {path:'metadata-extraction', loadChildren: () => import('./metadata-extraction/metadata-extraction.module').then(m => m.MetadataExtractionModule)}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
