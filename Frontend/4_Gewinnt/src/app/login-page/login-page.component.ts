import { Component, Input } from '@angular/core';
import { Router, Routes } from '@angular/router';
import { MainPageComponent } from '../main-page/main-page.component';
import { NetworkBackendComponent } from '../network-backend/network-backend.component';
import { HttpClient } from '@angular/common/http';
const appRoutes:Routes=[
  { path: 'Main-Page', component: MainPageComponent }
]

@Component({
  selector: 'app-login-page',
  templateUrl: './login-page.component.html',
  styleUrls: ['./login-page.component.css']
})
export class LoginPageComponent {
  constructor(public router:Router, public network:NetworkBackendComponent){

  }

  onSelect( User:String, psw:String): void {
    console.log(User,psw+" test")
    var bool = this.network.Autherisation(JSON.parse('{ "username": "admin", "password":"admin" }'));
    
    console.log(bool)
    
  }

    
  

}
