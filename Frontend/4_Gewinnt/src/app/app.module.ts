import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginPageComponent } from './login-page/login-page.component';
import { MainPageComponent } from './main-page/main-page.component';
import { NetworkBackendComponent } from './network-backend/network-backend.component';
import { VierGewinntSpielComponent } from './vier-gewinnt-spiel/vier-gewinnt-spiel.component';
import { UserCreationComponent } from './user-creation/user-creation.component';
import { RoutingComponent } from './routing/routing.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginPageComponent,
    MainPageComponent,
    NetworkBackendComponent,
    VierGewinntSpielComponent,
    UserCreationComponent,
    
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [RoutingComponent],
  bootstrap: [AppComponent]
})
export class AppModule { }
