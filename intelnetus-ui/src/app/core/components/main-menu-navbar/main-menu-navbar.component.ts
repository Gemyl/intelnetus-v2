import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { state, transition, style, animate, trigger } from '@angular/animations';
import { faHome, faSearch, faGlobe, faGear, faInfo } from '@fortawesome/free-solid-svg-icons';

@Component({
    selector: 'app-main-menu-navbar',
    templateUrl: './main-menu-navbar.component.html',
    styleUrls: ['./main-menu-navbar.component.scss'],
    animations: [
        trigger('draw', [
            state('drawIn', style({
                width: '0px',
            })),
            state('drawOut', style({
                width: '120px'
            })),
            transition('drawIn => drawOut', animate('0.3s')),
            transition('drawOut => drawIn', animate('0.3s'))
        ])
    ],
    standalone: false
})

export class MainMenuNavbarComponent implements OnInit {
  @ViewChild("mainNavbar") navbar: ElementRef;
  public mainMenuIconsHovered = false;
  public mainMenuTitlesHovered = false;
  public showMenuItemsTitles = false;

  faHome = faHome;
  faSearch = faSearch;
  faGlobe =faGlobe;
  faGear = faGear;
  faInfo = faInfo;
  
  constructor(
    private router: Router
  ) {}

  ngOnInit(): void {
  }

  navigate(route: number) {
    
    switch(route) {
      case 0:
        this.router.navigate(['/']);
        break;
      
      case 1:
        this.router.navigate(['/metadata-extraction']);
        break;

      default:
        this.router.navigate(['/', '']);
    }

  }

  toggleMainMenuNavbar() {
    this.showMenuItemsTitles = true;
  }

  closeMainMenuNavbar() {
    this.showMenuItemsTitles = false;
  }

  onHoverMainMenu(code: number) {
    switch(code) {
      case 0:
        this.mainMenuIconsHovered = true;
        break;

      case 1:
        setTimeout(() => {
          this.mainMenuIconsHovered = false;
        });
        break;
      
      case 2:
        this.mainMenuTitlesHovered = true;
        break;

      case 3:
        this.mainMenuTitlesHovered = false;
        break;

      default:
        this.mainMenuIconsHovered = false;
        this.mainMenuTitlesHovered = false;
    }
  }

}
