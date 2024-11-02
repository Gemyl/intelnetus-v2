import { Component, ViewEncapsulation, OnInit } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { faBook, faUser, faBuilding } from '@fortawesome/free-solid-svg-icons';
import { AuthorVariants, OrganizationVariants, PublicationVariants, Variants, Entity } from '../../models/metadata-extraction.model';

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

    this.selectedVariants.forEach(sv => {
      switch(sv.type) {
        case Entity.PUBLICATION:
          let publicationVariant = this.variants.publicationsVariants.originals.find(pv => pv.id == sv.id);

          if(!publicationVariant) {
            publicationVariant = this.variants.publicationsVariants.duplicates.find(pv => pv.id == sv.id);
          }

          publicationVariant.selected = true;
          
          break;

        case Entity.AUTHOR:
          let authorVariant = this.variants.authorsVariants.originals.find(av => av.id == sv.id);

          if(!authorVariant) {
            authorVariant = this.variants.authorsVariants.duplicates.find(av => av.id == sv.id);
          }

          authorVariant.selected = true;
          
          break;

        case Entity.ORGANIZATION:
          let organizationVariant = this.variants.organizationsVariants.originals.find(ov => ov.id == sv.id);

          if(!organizationVariant) {
            organizationVariant = this.variants.organizationsVariants.duplicates.find(ov => ov.id == sv.id);
          }

          organizationVariant.selected = true;
          
          break;

        default:
          // do nothing
      }
    });
  }

  onSelectAllPublicationsVariants(event: any, areOriginals: boolean) {
    if(areOriginals) {
      if(event.target.checked) {
        this.variants.publicationsVariants.originals.forEach(v => {
          v.selected = true;
          this.selectedVariants.push(v);
        });
      } else {
        this.variants.publicationsVariants.originals.forEach(v => {
          v.selected = false;
          this.selectedVariants = this.selectedVariants.filter(sv => sv.id != v.id);
        });
      }
    } else {
      if(event.target.checked) {
        this.variants.publicationsVariants.duplicates.forEach(v => {
          v.selected = true;
          this.selectedVariants.push(v);
        });
      } else {
        this.variants.publicationsVariants.duplicates.forEach(v => {
          v.selected = false;
          this.selectedVariants = this.selectedVariants.filter(sv => sv.id != v.id);
        });
      }
    }
  }

  onSelectAllAuthorsVariants(event: any, areOriginals: boolean) {
    if(areOriginals) {
      if(event.target.checked) {
        this.variants.authorsVariants.originals.forEach(v => {
          v.selected = true;
          this.selectedVariants.push(v);
        });
      } else {
        this.variants.authorsVariants.originals.forEach(v => {
          v.selected = false;
          this.selectedVariants = this.selectedVariants.filter(sv => sv.id != v.id);
        });
      }
    } else {
      if(event.target.checked) {
        this.variants.authorsVariants.duplicates.forEach(v => {
          v.selected = true;
          this.selectedVariants.push(v);
        });
      } else {
        this.variants.authorsVariants.duplicates.forEach(v => {
          v.selected = false;
          this.selectedVariants = this.selectedVariants.filter(sv => sv.id != v.id);
        });
      }
    }
  }

  onSelectAllOrganizationsVariants(event: any, areOriginals: boolean) {
    if(areOriginals) {
      if(event.target.checked) {
        this.variants.organizationsVariants.originals.forEach(v => {
          v.selected = true;
          this.selectedVariants.push(v);
        });
      } else {
        this.variants.organizationsVariants.originals.forEach(v => {
          v.selected = false;
          this.selectedVariants = this.selectedVariants.filter(sv => sv.id != v.id);
        });
      }
    } else {
      if(event.target.checked) {
        this.variants.organizationsVariants.duplicates.forEach(v => {
          v.selected = true;
          this.selectedVariants.push(v);
        });
      } else {
        this.variants.organizationsVariants.duplicates.forEach(v => {
          v.selected = false;
          this.selectedVariants = this.selectedVariants.filter(sv => sv.id != v.id);
        });
      }
    }
  }

  onSelectVariant(event: any, item: PublicationVariants) {
    if(event.target.checked) {
      this.selectedVariants.push(item);
    } else {
      this.selectedVariants = this.selectedVariants.filter(sv => sv.id != item.id);
    }
  }

  onClose(data: Array<{id: string}> = []) {
    this.activeModal.close(data);
  }

  onSubmit() {
    const mappedVariants = this.selectedVariants.map((v) => ({id: v.id, type: v.type}));
    this.onClose(mappedVariants);
  }
}
