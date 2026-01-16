import { Component, Input } from '@angular/core';
import { Link, Node } from '../../models/metadata-network.model';

@Component({
  selector: 'app-metadata-network',
  standalone: false,
  templateUrl: './metadata-network.component.html',
  styleUrl: './metadata-network.component.scss'
})
export class MetadataNetworkComponent {
  @Input() nodes: Array<Node> = [];
  @Input() links: Array<Link> = [];

  constructor() {}
}
