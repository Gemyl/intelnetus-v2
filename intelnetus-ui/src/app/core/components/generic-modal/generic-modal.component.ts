import { Component, EventEmitter, Input, Output } from '@angular/core';
import { faTimes } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'generic-modal',
  standalone: false,
  templateUrl: './generic-modal.component.html',
  styleUrls: []
})
export class GenericModalComponent {
  @Output() onSubmitClicked: EventEmitter<null> = new EventEmitter<null>();
  @Output() onSecondClicked: EventEmitter<null> = new EventEmitter<null>();
  @Output() onCloseClicked: EventEmitter<null> = new EventEmitter<null>();
  @Input() title: string;
  @Input() showSubmitButton: boolean = true;
  @Input() showSecondButton: boolean = true;
  @Input() enableSubmitButton: boolean = true;
  @Input() enableSecondButton: boolean = true;
  @Input() submitButtonLabel: string = "Submit";
  @Input() secondButtonLabel: string = "";
  @Input() closeOnSubmit: boolean = false;

  faTimes = faTimes;

  onSubmit() {
    this.onSubmitClicked.emit();
  }

  onSecondButtonClicked() {
    this.onSecondClicked.emit();
  }

  onClose() {
    this.onCloseClicked.emit();
  }
}
