import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { DataService } from '../services/data.service';

@Component({
  selector: 'app-recent-captured-frames',
  templateUrl: './recent-captured-frames.component.html',
  styleUrls: ['./recent-captured-frames.component.scss']
})
export class RecentCapturedFramesComponent implements OnInit {


  $recent_captured_frames: any;

  constructor(private data: DataService) {
  }

  ngOnInit() {
    this.data.getRecentCapturedFrames().subscribe(
      data => this.$recent_captured_frames = data
    );
  }

}
