import { NgModule } from '@angular/core';
import { Router, RouterModule, Routes } from '@angular/router';
import { LoginPageComponent } from './login-page/login-page.component';
import { MainPageComponent } from './main-page/main-page.component';
import { HttpClientModule } from '@angular/common/http';
import { VierGewinntSpielComponent } from './vier-gewinnt-spiel/vier-gewinnt-spiel.component';
import { UserCreationComponent } from './user-creation/user-creation.component';
const routes: Routes = [

    { path: '', redirectTo: '/Login-Page', pathMatch: 'full' },


  { path: 'Login-Page', component: LoginPageComponent },
  { path: 'Main-Page', component: MainPageComponent },
  { path: 'vier-gewinnt-spiel', component: VierGewinntSpielComponent },
  { path: 'User-Creation', component: UserCreationComponent }
];

@NgModule({
  imports: [HttpClientModule,RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {



 }
