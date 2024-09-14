import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MainMenuNavbarComponent } from './components/main-menu-navbar/main-menu-navbar.component';
import { CoreComponent } from './core.component';
import { WebColors } from './models/web-colors.model';
import { ControlBarComponent } from './components/control-bar/control-bar.component';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';

@NgModule({
  declarations: [
    CoreComponent,
    MainMenuNavbarComponent,
    ControlBarComponent
  ],
  imports: [
    CommonModule,
    FontAwesomeModule
  ],
  exports: [
    MainMenuNavbarComponent,
    ControlBarComponent
  ],
  providers: [
    WebColors
  ]
})
export class CoreModule { }
