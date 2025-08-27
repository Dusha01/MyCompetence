import { defaultHeaderConfig, type HeaderConfig } from './HeaderConfig';

const API_URL = '/api/admin/header';

export async function loadHeaderConfig(): Promise<HeaderConfig> {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) throw new Error('Failed to load header config');
        return await response.json();
    } catch (error) {
        console.error('Using default header config due to error:', error);
        return { ...defaultHeaderConfig };
    }
}

export async function saveHeaderConfig(config: HeaderConfig): Promise<boolean> {
    try {
        const response = await fetch(API_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(config)
        });
        return response.ok;
    } catch (error) {
        console.error('Failed to save header config:', error);
        return false;
    }
}