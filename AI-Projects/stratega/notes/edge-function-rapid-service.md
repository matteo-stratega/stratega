import { serve } from "https://deno.land/std@0.168.0/http/server.ts"

serve(async (req) => {
  const testData = {
    "gpt_language": ["English"],
    "company_data": {
      "company_info": "Stratega builds repeatable systems for B2B lead generation and sales ops. We help startups replace ad-dependent growth with systematic outbound engines.",
      "company_language": "English",
      "company_location": "Europe",
      "company_url": "https://stratega.co",
      "company_competitors": [],
      "content_generation_instruction": "Write like a growth operator sharing insights with a peer. Use specific numbers. Short sentences. Open with contrarian takes. Include concrete examples. Avoid buzzwords and filler phrases."
    },
    "blog_page": {
      "primary_keyword": "B2B lead generation without ads",
      "links": "<a href='/services/growth-consulting'>Growth Consulting</a>",
      "company_url": "https://stratega.co",
      "company_name": "Stratega"
    }
  }

  return new Response(
    JSON.stringify(testData),
    { headers: { "Content-Type": "application/json" } }
  )
})
