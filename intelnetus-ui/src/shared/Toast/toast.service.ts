import { Injectable } from '@angular/core';
import { MessageType, Toast } from './toast.model';

@Injectable({
  providedIn: 'root'
})
export class ToastService {
  public toasts: Toast[] = [];

  constructor() { }

  show(toast: Toast) {
    switch (toast.type) {
      case MessageType.SUCCESS:
        toast.header = "";
        toast.icon = "check";
        break;

      case MessageType.ERROR:
        toast.header = "";
        toast.icon = "times";
        break;

      case MessageType.INFO:
        toast.header = "";
        toast.icon = "info"
        break;

      case MessageType.WARNING:
        toast.header = "";
        toast.icon = "exclamation";
        break;

      default:
        toast.header = "";
    }
    this.toasts.push(toast);
  }

  remove(toast: Toast) {
    this.toasts = this.toasts.filter((t) => t != toast);
  }
}
