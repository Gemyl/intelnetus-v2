import { Component, ViewEncapsulation, OnInit } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { faBook, faUser, faBuilding } from '@fortawesome/free-solid-svg-icons';
import { AuthorVariants, OrganizationVariants, PublicationVariants, Variants } from '../../models/metadata-extraction.model';

@Component({
  selector: 'app-variants-modal',
  templateUrl: './variants-modal.component.html',
  styleUrl: './variants-modal.component.scss',
  encapsulation: ViewEncapsulation.None
})
export class VariantsModalComponent implements OnInit {
  faBook = faBook;
  faUser = faUser;
  faBuilding = faBuilding;
  
  public variants: Variants;
  public selectedVariants: Array<PublicationVariants | AuthorVariants | OrganizationVariants> = [];
  public pageSize: number = 5;

  constructor(
    public activeModal: NgbActiveModal
  ) {}

  ngOnInit(): void {
    let temp = this.variants;
  }

  onClose(data: Array<{id: string}> = []) {
    this.activeModal.close(data);
  }

  onSubmit() {
    const mappedVariants = this.selectedVariants.map((v) => ({id: v.id, type: v.type}));
    this.onClose(mappedVariants);
  }
}
