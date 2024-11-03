import { Component } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-view-details',
  templateUrl: './view-details.component.html'
})

export class ViewDetailsComponent {
  public title: string;
  public text: string;

  constructor(
    private _activeModal: NgbActiveModal
  ) {}

  onClose() {
    this._activeModal.close();
  }
}
