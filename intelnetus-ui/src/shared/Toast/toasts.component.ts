import { Component } from '@angular/core';
import { ToastService } from './toast.service';

@Component({
    selector: 'app-toasts',
    templateUrl: './toasts.component.html',
    styleUrl: './toasts.component.scss',
    standalone: false
})
export class ToastsComponent {

  constructor(
    public _toastService: ToastService
  ) {}
}
