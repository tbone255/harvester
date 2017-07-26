import { ModuleWithProviders } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { AppComponent } from './app.component';
import { HomeComponent } from './components/home/home.component';
import { AddComponent } from './components/add/add.component';
import { InventoryComponent } from './components/inventory/inventory.component';
import { AboutComponent } from './components/about/about.component';
import { AdminComponent } from './components/admin/admin.component';

export const router: Routes = [
	{ path: '', redirectTo: 'home', pathMatch: 'full' },
	{ path: 'home', component: HomeComponent },
	{ path: 'add', component: AddComponent },
	{ path: 'inventory', component: InventoryComponent },
	{ path: 'about', component: AboutComponent },
	{ path: 'admin', component: AdminComponent },

];

export const routes: ModuleWithProviders = RouterModule.forRoot(router);