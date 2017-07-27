import { ModuleWithProviders } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { AppComponent } from './app.component';
import { HomeComponent } from './components/home/home.component';
import { InventoryComponent } from './components/inventory/inventory.component';
import { AboutComponent } from './components/about/about.component';
import { AdminComponent } from './components/admin/admin.component';
import { AddPlantComponent } from './components/add-plant/add-plant.component';

export const router: Routes = [
	{ path: '', redirectTo: 'home', pathMatch: 'full' },
	{ path: 'home', component: HomeComponent },
	{ path: 'inventory', component: InventoryComponent },
	{ path: 'about', component: AboutComponent },
	{ path: 'admin', component: AdminComponent },
	{ path: 'add-plant', component: AddPlantComponent },
];

export const routes: ModuleWithProviders = RouterModule.forRoot(router);