import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, FormBuilder, FormArray, Validators, ValidatorFn, AbstractControl, ValidationErrors } from '@angular/forms';
import { GetMetadataRequest } from '../../models/metadata-extraction.model';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { faTrash } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-metadata-search-form',
  templateUrl: './metadata-search-form.component.html',
  styleUrls: []
})
export class MetadataSearchFormComponent implements OnInit {
  public searchForm: FormGroup;
  public operatorsOptions: string[] = ['AND','OR','AND NOT'];
  public fieldsOptions: any[] = [
    { id: "0", name: "Agricultural and Biological Sciences", selected: false },
    { id: "1", name: "Arts and Humanities", selected: false },
    { id: "2", name: "Biochemistry Genetics and Molecular Biology", selected: false },
    { id: "3", name: "Business, Management, and Accounting", selected: false },
    { id: "4", name: "Chemical Engineering", selected: false },
    { id: "5", name: "Chemistry", selected: false },
    { id: "6", name: "Computer Science", selected: false },
    { id: "7", name: "Decision Sciences", selected: false },
    { id: "8", name: "Dentistry", selected: false },
    { id: "9", name: "Earth and Planetary Sciences", selected: false },
    { id: "10", name: "Economics, Econometrics and Finance", selected: false },
    { id: "11", name: "Energy", selected: false },
    { id: "12", name: "Engineering", selected: false },
    { id: "13", name: "Environmental Science", selected: false },
    { id: "14", name: "Health Professions", selected: false },
    { id: "15", name: "Immunology and Microbiology", selected: false },
    { id: "16", name: "Materials Science", selected: false },
    { id: "17", name: "Mathematics", selected: false },
    { id: "18", name: "Medicine", selected: false },
    { id: "19", name: "Multidisciplinary", selected: false },
    { id: "20", name: "Neuroscience", selected: false },
    { id: "21", name: "Nursing", selected: false },
    { id: "22", name: "Pharmacology, Toxicology, and Pharmaceutics", selected: false },
    { id: "23", name: "Physics and Astronomy", selected: false },
    { id: "24", name: "Psychology", selected: false },
    { id: "25", name: "Social Sciences", selected: false },
    { id: "26", name: "Veterinary", selected: false }
  ];

  faTrash = faTrash;

  constructor(
    private activeModal: NgbActiveModal,
    private _fb: FormBuilder
  ) {
    this.searchForm = this._fb.group({
      keywords: this._fb.array([this._fb.group(
        {
          value: new FormControl("", Validators.required), 
          operator: new FormControl("")
        },
      )]),
      startYear: this._fb.control("", Validators.required),
      endYear: this._fb.control("", Validators.required),
      fields: this._fb.array(
        this.fieldsOptions.map(f => this._fb.group({
          id: new FormControl(f.id),
          name: new FormControl(f.name),
          selected: new FormControl(f.selected)
        }))
      )
    });
  }

  get fields() {
    return this.searchForm.get("fields") as FormArray;
  }

  get keywords() {
    return this.searchForm.get("keywords") as FormArray;
  }

  ngOnInit(): void {}

  addKeywordBlock() {
    this.keywords.push(this._fb.group({
      value: new FormControl("", Validators.required),
      operator: new FormControl("AND")
    }));
  }

  removeKeywordBlock(index: number) {
    this.keywords.removeAt(index);
  }

  onFormSubmit() {
    const keywords: string = this.keywords.controls.map(k => k.value.value).join(",");
    const operators: string = this.keywords.controls.filter(f => f.value.operator).map(k => k.value.operator).join(",");
    const startYear: string = this.searchForm.get("startYear").value;
    const endYear: string = this.searchForm.get("endYear").value;
    const fields: string = this.fields.controls.filter(f => f.value.selected).map(f => f.value.id).join(",");

    const requestBody = {
      keywords: keywords,
      operators: operators,
      startYear: startYear,
      endYear: endYear,
      fields: fields
    }; 

    this.closeModal(requestBody);
  }

  closeModal(response?: Partial<GetMetadataRequest>) {
    this.activeModal.close(response);
  }

}
