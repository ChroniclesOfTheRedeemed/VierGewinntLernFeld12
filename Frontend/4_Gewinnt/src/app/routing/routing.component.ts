import { Component } from '@angular/core';
import { Router, ActivatedRoute, ParamMap, Routes } from '@angular/router';

@Component({
  selector: 'app-routing',
  templateUrl: './routing.component.html',
  styleUrls: ['./routing.component.css']
})
export class RoutingComponent {
  name: any;
  constructor(
    private route: ActivatedRoute,private router:Router
  ) {}
  
  ngOnInit() {
    this.route.queryParams.subscribe(params => {
      this.name = params['/Login-Page'];
    });



  }
  public routetoMain(){
    this.router.navigate(['/Main-Page'])
  }
  
}
