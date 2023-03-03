import { Component } from '@angular/core';
import { Router, } from '@angular/router';

import { LoginPageComponent } from './login-page/login-page.component';
import { Routes } from '@angular/router';
import { MainPageComponent } from './main-page/main-page.component';
import { RoutingComponent } from './routing/routing.component';
const appRoutes:Routes=[
  { path: 'Login-Page', component: LoginPageComponent },
  { path: 'Main-Page', component: MainPageComponent }
]

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  title = '4_Gewinnt';
  constructor(private router:Router,private routing:RoutingComponent){
    this.router.navigate(["/Login-Page"])
  }
  
  ngOnInit(){

    this.routing.ngOnInit();
  }

  redirectTo(uri:string){
    this.router.navigateByUrl('/', {skipLocationChange: true}).then(()=>
    this.router.navigate([uri]));
 }
}

function RouteConfig(arg0: { path: string; redirectTo: string; }[]) {
  throw new Error('Function not implemented.');
}

