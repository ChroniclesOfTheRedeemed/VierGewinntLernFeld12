import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NetworkBackendComponent } from './network-backend.component';

describe('NetworkBackendComponent', () => {
  let component: NetworkBackendComponent;
  let fixture: ComponentFixture<NetworkBackendComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ NetworkBackendComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NetworkBackendComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
