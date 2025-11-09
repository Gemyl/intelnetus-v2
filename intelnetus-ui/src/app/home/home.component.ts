import { Component, OnInit } from '@angular/core';
import {
  faGlobe,
  faCogs,
  faGraduationCap, 
  faNetworkWired,
  faChartBar,
  faDownload 
} from '@fortawesome/free-solid-svg-icons';
import { 
  state,
  trigger,
  style,
  transition,
  animate
} from '@angular/animations';

@Component({
    selector: 'app-home',
    templateUrl: './home.component.html',
    styleUrls: [],
    animations: [
        trigger('cardHover', [
            state('hovered', style({ transform: 'scale(1.1)', background: 'linear-gradient(to top left, #dddddd, #579657)', color: 'white' })),
            state('notHovered', style({ transform: 'scale(1)', backgroundColor: '#eeeeee', color: 'black' })),
            transition('* <=> *', animate('200ms'))
        ])
    ],
    standalone: false
})

export class HomeComponent implements OnInit {
  faGlobe = faGlobe;
  faCogs = faCogs;
  faGraduationCap = faGraduationCap;
  faNetworkWired = faNetworkWired;
  faChartBar = faChartBar;
  faDownload = faDownload;

  public cards: Array<any> = [
    {icon: faGlobe, hoverState: "notHovered", text: "Access to metrics of publications and researchers that have been unified from world\'s leading scientific bibliography databases."},
    {icon: faCogs, hoverState: "notHovered", text: "Duplicate detection algorithms are directed to minimize possible flaws and inconsistencies for greater data quality and reliability."},
    {icon: faGraduationCap, hoverState: "notHovered", text: "Search for scientific publications from a wide range of disciplines, subjected areas and scientific fields."},
    {icon: faNetworkWired, hoverState: "notHovered", text: "Based on raw bibliographic data, indices about correlations and their efficiency inside the scientific community are calculated and provided for knowledge networks analysis."},
    {icon: faChartBar, hoverState: "notHovered", text: "Enrich your scientometrics analysis with a visualized overview of your search's insights through various graphs and charts."},
    {icon: faDownload, hoverState: "notHovered", text: "Download your search results in your machine in Excel or CSV files to expand their usability in any way you prefer!"}
  ];

  ngOnInit(): void {
    this.cards.forEach(c => c.hoverState = "notHovered");
  }

}
