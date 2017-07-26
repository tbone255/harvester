import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { NavbarComponent } from './components/navbar/navbar.component';
import { HomeComponent } from './components/home/home.component';
import { InventoryComponent } from './components/inventory/inventory.component';
import { AboutComponent } from './components/about/about.component';
import { AdminComponent } from './components/admin/admin.component';

import { routes } from './app.router';
import { AddComponent } from './components/add/add.component';
import { AddDropdownComponent } from './components/add-dropdown/add-dropdown.component';

@NgModule({
  declarations: [
    AppComponent, NavbarComponent, HomeComponent, InventoryComponent, AboutComponent, AdminComponent, AddComponent, AddDropdownComponent
  ],
  imports: [
    BrowserModule,
    routes
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
