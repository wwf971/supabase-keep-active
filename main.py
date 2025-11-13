
# pip install supabase
import os
# your supabase project's url
os.environ['SUPABASE_URL'] = 'https://ehxlalrrjkrkdrayksnj.supabase.co'
# your supabase project's api key
os.environ['SUPABASE_KEY'] = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVoeGxhbHJyamtya2RyYXlrc25qIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjE3NDAyNDUsImV4cCI6MjA3NzMxNjI0NX0.tTBh0-oXhnnPuPAhhprEoYrg702Wdm9z7WjW05kiRkA'

from supabase import create_client, Client
from datetime import datetime

def create_activity_table():

    print("Please create the activity_log table first by running the SQL above in your Supabase dashboard.")
    print("Table structure:")
    print("  - id: SERIAL PRIMARY KEY")
    print("  - timestamp: TIMESTAMP WITH TIME ZONE DEFAULT NOW()")
    print("  - message: TEXT DEFAULT 'Keep-alive ping'")

def main():
    # Supabase credentials - set these as environment variables
    supabase_url = os.getenv('SUPABASE_URL')
    supabase_key = os.getenv('SUPABASE_KEY')

    if not supabase_url or not supabase_key:
        print("Error: Please set SUPABASE_URL and SUPABASE_KEY environment variables")
        print("You can find these in your Supabase project settings > API")
        return

    try:
        # Initialize Supabase client
        supabase: Client = create_client(supabase_url, supabase_key)

        # Insert a keep-alive row
        insert_data = {
            'timestamp': datetime.utcnow().isoformat(),
            'message': 'Automated keep-alive ping to prevent project inactivation'
        }

        result = supabase.table('activity_log').insert(insert_data).execute()
        print(f"Inserted keep-alive row with ID: {result.data[0]['id']}")
        print("Supabase project activity maintained!")

    except Exception as e:
        error_msg = str(e)
        if "relation \"activity_log\" does not exist" in error_msg.lower():
            print("Error: The activity_log table doesn't exist yet.")
            create_activity_table()
        else:
            print(f"Error: {error_msg}")
            print("Make sure you have the supabase-py library installed: pip install supabase")

if __name__ == "__main__":
    main()
