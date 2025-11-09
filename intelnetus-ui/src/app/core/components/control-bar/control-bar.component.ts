import { Component } from '@angular/core';
import { faSearch } from '@fortawesome/free-solid-svg-icons';

@Component({
    selector: 'app-control-bar',
    templateUrl: './control-bar.component.html',
    styleUrls: [],
    standalone: false
})
export class ControlBarComponent {
  faSearch = faSearch;
}
