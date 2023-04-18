import { Component } from '@angular/core';
import { NetworkBackendComponent } from '../network-backend/network-backend.component';

@Component({
  selector: 'app-vier-gewinnt-spiel',
  templateUrl: './vier-gewinnt-spiel.component.html',
  styleUrls: ['./vier-gewinnt-spiel.component.css']
})
export class VierGewinntSpielComponent {
  constructor(private network:NetworkBackendComponent){

  }
  test!:string;
  td!: string;
  Player!: Number;
  Column!: Number;
  Row!: Number;
  button(number:number){
    this.network.GameMove(number);
    
    

  }
  
  fetchGameState(){

  }
}
