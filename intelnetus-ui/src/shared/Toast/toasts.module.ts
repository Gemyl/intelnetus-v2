import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ToastsComponent } from './toasts.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { ToastService } from './toast.service';

@NgModule({
  declarations: [
    ToastsComponent
  ],
  imports: [
    CommonModule,
    NgbModule
  ],
  providers: [
    ToastService
  ],
  exports: [
    ToastsComponent
  ]
})
export class ToastsModule { }
