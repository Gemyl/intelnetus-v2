import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CoreModule } from './core/core.module';
import { HomeModule } from './home/home.module';
import { MetadataExtractionModule } from './metadata-extraction/metadata-extraction.module';
import { StoreModule } from '@ngrx/store';
import { EffectsModule } from '@ngrx/effects';
import { ToastsModule } from 'src/shared/Toast/toasts.module';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    AppRoutingModule,
    CoreModule,
    HomeModule,
    MetadataExtractionModule,
    StoreModule.forRoot({}),
    EffectsModule.forRoot({}),
    ToastsModule
],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
