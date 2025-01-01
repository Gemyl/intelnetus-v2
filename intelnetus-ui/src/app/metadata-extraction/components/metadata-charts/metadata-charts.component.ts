import { Component, OnInit, Input, ChangeDetectionStrategy } from '@angular/core';
import { Chart } from 'chart.js/auto';
import { Store } from '@ngrx/store';
import { AppState } from 'src/app/app.state';

@Component({
  selector: 'app-metadata-charts',
  templateUrl: './metadata-charts.component.html',
  styleUrl: './metadata-charts.component.scss'
})
export class MetadataChartsComponent implements OnInit {
  public publicationsPerCountryChart: Chart;
  public publicationsCitationsPerFieldChart: Chart;
  public fieldsCitationsPerYearChart: Chart;

  constructor(
    private store$: Store<AppState>
  ) {}

  ngOnInit(): void {
    this.store$
      .select((store) => store.metadataInsightsState)
      .subscribe((metadataInsightsState) => {
        // publications number per country
        let countries: Array<string> = [];
        let publicationsNumberPerCountry: Array<number> = [];

        if(Object.keys(metadataInsightsState.publicationsNumberPerCountry).length > 0) {
          countries = Object.keys(metadataInsightsState.publicationsNumberPerCountry);
          publicationsNumberPerCountry = Object.values(metadataInsightsState.publicationsNumberPerCountry);
        }

        this.publicationsPerCountryChart.data.labels = countries;
        this.publicationsPerCountryChart.data.datasets = [{
          data: publicationsNumberPerCountry
        }];

        this.publicationsPerCountryChart.update();

        // publications number per field
        let fields: Array<string> = [];
        let citationsNumberPerField: Array<{label: string, data: Array<number>}> = [];

        if(Object.keys(metadataInsightsState.publicationsCitationsNumberPerField).length > 0) {
          fields = Object.keys(metadataInsightsState.publicationsCitationsNumberPerField);
          citationsNumberPerField = [{label: "Citations", data: Object.values(metadataInsightsState.publicationsCitationsNumberPerField)}];
        }

        this.publicationsCitationsPerFieldChart.data.labels = fields;
        this.publicationsCitationsPerFieldChart.data.datasets = citationsNumberPerField;

        this.publicationsCitationsPerFieldChart.update();

        // fields citations per year
        let years: Array<string> = [];
        let fieldsCitationsPerYear: Array<{label: string, data: Array<number>}> = [];

        if(Object.keys(metadataInsightsState.fieldsCitationsPerYear).length > 0) {
          Object.keys(metadataInsightsState.fieldsCitationsPerYear).forEach((field) => {
            if(Object.keys(metadataInsightsState.fieldsCitationsPerYear).indexOf(field) == 0) {
              years = Object.keys(metadataInsightsState.fieldsCitationsPerYear[field]);
            }
  
            fieldsCitationsPerYear.push({
              label: field,
              data: Object.values(metadataInsightsState.fieldsCitationsPerYear[field])
            })
          });
        }

        this.fieldsCitationsPerYearChart.data.labels = years;
        this.fieldsCitationsPerYearChart.data.datasets = fieldsCitationsPerYear;

        this.fieldsCitationsPerYearChart.update(); 
      })

    this.publicationsPerCountryChart = new Chart("publications-per-country-chart", {
      type: "doughnut",
      data: {
        labels: [],
        datasets: []
      },
      options: {
        plugins: {
          legend: {
            fullSize: true,
            position: "top",
            title: {
              display: true,
              text: "Publications Number Per Country",
              font: {
                weight: "bolder"
              }
            }
          }
        },
        maintainAspectRatio: false
      }
    });

    this.publicationsCitationsPerFieldChart = new Chart("publications-citations-per-field-chart", {
      type: "bar",
      data: {
        labels: [],
        datasets: []
      },
      options: {
        plugins: {
          legend: {
            position: "top",
            title: {
              display: true,
              text: "Publications Number Per Field",
              font: {
                weight: "bolder"
              }
            }
          }
        },
        maintainAspectRatio: false
      }
    });

    this.fieldsCitationsPerYearChart = new Chart("fields-citations-per-year-chart", {
      type: "line",
      data: {
        labels: [],
        datasets: []
      },
      options: {
        plugins: {
          legend: {
            display: true,
            title: {
              text: "Fields Citations Per Year",
              display: true,
              font: {
                weight: "bolder"
              }
            }
          }
        },
        maintainAspectRatio: false
      }
    });
  }
  
}
