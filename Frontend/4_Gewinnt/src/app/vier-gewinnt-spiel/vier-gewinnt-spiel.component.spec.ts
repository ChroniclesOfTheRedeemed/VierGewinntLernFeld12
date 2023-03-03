import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VierGewinntSpielComponent } from './vier-gewinnt-spiel.component';

describe('VierGewinntSpielComponent', () => {
  let component: VierGewinntSpielComponent;
  let fixture: ComponentFixture<VierGewinntSpielComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ VierGewinntSpielComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(VierGewinntSpielComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
