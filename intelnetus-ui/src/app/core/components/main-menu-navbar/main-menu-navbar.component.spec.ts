import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MainMenuNavbarComponent } from './main-menu-navbar.component';
import { DebugElement } from '@angular/core';

describe('MainMenuNavbarComponent', () => {
  let component: MainMenuNavbarComponent;
  let fixture: ComponentFixture<MainMenuNavbarComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [MainMenuNavbarComponent]
    });
    fixture = TestBed.createComponent(MainMenuNavbarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should generate navbar', () => {
    const debugElement: DebugElement = fixture.debugElement;
    const nativeElement: HTMLElement = debugElement.nativeElement;
    const container = nativeElement.getElementsByClassName('container');
    const mainMenuIcons = nativeElement.getElementsByClassName('main-menu-icons');
    const mainMenuTitles = nativeElement.getElementsByClassName('main-menu-titles');

    expect(container.length).toEqual(1);
    expect(mainMenuIcons.length).toEqual(1);
    expect(mainMenuTitles.length).toEqual(1);
  })
});
