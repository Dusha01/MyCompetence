import { writable } from 'svelte/store';
import { browser } from '$app/environment';

interface AdminData {
    username: string;
    email: string;
}

interface AuthState {
    token: string | null;
    adminData: AdminData | null;
    isAuthenticated: boolean;
    error: string | null;
}

export const authStore = writable<AuthState>({
    token: null,
    adminData: null,
    isAuthenticated: false,
    error: null
});

export const initializeAuth = () => {
    if (browser) {
        const token = sessionStorage.getItem('admin_token');
        if (token) {
            authStore.update(state => ({
                ...state,
                token,
                isAuthenticated: true
            }));
        }
    }
};