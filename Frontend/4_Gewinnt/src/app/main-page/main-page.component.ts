import { Component } from '@angular/core';
import { Router, Routes } from '@angular/router';
import { LoginPageComponent } from '../login-page/login-page.component';
import { NetworkBackendComponent } from '../network-backend/network-backend.component';
import { VierGewinntSpielComponent } from '../vier-gewinnt-spiel/vier-gewinnt-spiel.component';
const appRoutes:Routes=[
  { path: 'vier-gewinnt-spiel', component: VierGewinntSpielComponent },

]
@Component({
  selector: 'app-main-page',
  templateUrl: './main-page.component.html',
  styleUrls: ['./main-page.component.css']
})
export class MainPageComponent {
  title = "vier Gewinnt Main Page"
  constructor(private router:Router, public network:NetworkBackendComponent){

  }

  logOut(){
    this.network.logOut();
  }
  onSelect(): void {
    this.network.RequestGame("solo");
    this.router.navigate(['/vier-gewinnt-spiel']);
  }
}
