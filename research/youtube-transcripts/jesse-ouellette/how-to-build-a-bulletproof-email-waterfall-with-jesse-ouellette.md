# How to Build a Bulletproof Email Waterfall with Jesse Ouellette
*Expert:* Jesse Ouellette
*YouTube:* https://www.youtube.com/watch?v=FSc54cRCdJk
*Published:* 2025-08-28

## Key Takeaways
- Bad data can damage outbound performance before copy is even tested.
- Email waterfall and verification strategy are core parts of cold email infrastructure.
- Deliverability and enrichment decisions affect both reply rates and sender reputation.
- Jesse's source strengthens the list-building and infrastructure side of the pipeline.

---

## Full Transcript

[00:34] Are you
[00:48] Oh, this is going to be a good one,
[00:52] right?
[00:54] Oh, yeah. The gurus are not going to
[00:56] like it either.
[01:03] They're going to hate it. I I am I'm sad
[01:06] for them today because they're
[01:08] definitely not they never like my
[01:10] webinars for some reason. I don't know
[01:11] why, but they're definitely not going to
[01:13] like this one. I know that for sure.
[01:15] That's that's one of the problems with
[01:16] this one. This one will definitely get
[01:18] the gurus going. They're going to be
[01:20] very upset about this one.
[01:21] >> And this one is also fresh from the
[01:23] oven. So, it's it's uh it's a fresh
[01:26] stock we're going to bring to the table.
[01:30] >> So, it's so fresh. This is a this will
[01:32] be the I'll admit it. This is the
[01:34] freshest webinar I've ever done.
[01:36] >> Let's go.
[01:38] >> Stroke. It's a weird It's a weird thing
[01:40] that's happened today. We've uh we've
[01:43] gotten we've gotten weird
[01:45] >> on this one.
[01:47] >> There we go.
[01:49] >> Perfect. Uh we'll wait for people to
[01:51] come in, but again, hi, welcome to one
[01:54] more session of Smart Lead Officers. My
[01:56] name is Akash. I'm your customer success
[01:58] manager here at Smartle. So, we have the
[02:00] drill before we dive in. Take a second
[02:03] to click on the chatm icon at the bottom
[02:05] center of your screen. Drop a message
[02:07] telling us where you're tuning in from,
[02:09] how hot or cold it is where you are, and
[02:12] whether you're a part of an agency, a
[02:14] freelancer, or a SAS company. We'd love
[02:16] to know. Again, center bottom chat icon.
[02:19] Drop the comments.
[02:22] Ben Wright from Salt Lake.
[02:28] >> Ahmedabad, India, Spain. And can we try
[02:30] to standardize
[02:34] or Celsius either one? Just so we can
[02:36] all do the conversion.
[02:38] >> That's easier.
[02:40] Love
[02:40] >> these things.
[02:42] >> Colorado 17.
[02:45] >> Keep it coming.
[02:48] Bulgaria founder Silicon Valley B2B SAS.
[02:52] Awesome. Global global global as always.
[02:56] >> Yes. Portugal 27.
[03:01] >> What a great group, man. I'm excited.
[03:10] >> Smartle team always delivers on these
[03:12] things, too. That's one of the great
[03:14] things about working with Smartle. I've
[03:15] gone on a lot of webinars and, you know,
[03:17] this one really, they just always
[03:19] deliver. I feel uh Jesse, I think this
[03:22] one is going to be like more of the
[03:23] premium movie show where uh not
[03:26] everybody gets to watch it, but uh it's
[03:28] it's it's the newest movie ever, you
[03:30] know.
[03:31] >> Yep. We're recording it, right? We
[03:33] should charge for the recording after.
[03:35] Just just just
[03:48] >> awesome. We'll keep we'll let people
[03:50] coming in but let's kick start being
[03:52] respectful of all all of you who been
[03:54] there again uh for today's topic it's
[03:58] fresh outbone fails when your data is
[04:01] full of ghosts you pay for bad records
[04:05] send to empty seats tank deliverability
[04:08] and waste money Jesse doesn't need an
[04:11] introduction but Jesse is the founder of
[04:13] lead magic he helps B2B teams fix broken
[04:16] data workflows run outbound campaigns
[04:18] that actually land in inboxes. And
[04:21] today, Jesse is going to show us how to
[04:24] build a bulletproof email waterfall. The
[04:27] kind of one that verifies first, filters
[04:30] out ghost records, and wires directly
[04:32] into Smart Lead, so you only send to
[04:34] real people who actually reply. Jesse,
[04:37] over to you, sir. The floor is yours. A
[04:39] quick round of introduction and we can
[04:41] kickstart.
[04:43] >> Yeah. Well, hey, it's really great to
[04:46] see everybody. Uh, you know, I'm just
[04:49] super excited about this day today
[04:51] because I I I wanted to talk about this
[04:55] problem, uh, you know, very deeply here
[04:59] and use a lot of Clay. We love Clay.
[05:02] It's definitely our favorite tool. Uh,
[05:04] and our our email finder is in there.
[05:06] But there's a lot of unknown risks that
[05:09] people are taking right now and just
[05:11] want to introduce that today. But what
[05:13] we'll do is we'll turn it back over to
[05:15] the hosts and you guys can finish up and
[05:17] then I'll tell you when we'll uh you
[05:18] guys can start it.
[05:21] >> Yeah, but I think it's breaking up a
[05:24] little bit.
[05:28] >> Oh, is it
[05:30] >> a little bit a little choppy? But yeah,
[05:33] we can hear you fine. It's it's
[05:34] basically the video, but a little bit.
[05:36] >> Okay. Yeah.
[05:39] Okay, perfect. Here, let me tone down
[05:41] the video. Okay, can you hear me now?
[05:42] Yep. Loud and clear, sir.
[05:46] >> I might have to turn it off if I'm
[05:48] sharing uh just because of the not that
[05:50] I you know, it's not the pretty face
[05:51] you're here for your here for the data.
[05:53] So, anyways, we'll uh we'll move to it.
[05:55] But uh yeah, I'm on my uh mobile LTE so
[05:58] or 5G or whatever.
[06:00] >> Understood. Understood. But kickstarting
[06:02] Jesse, uh the first section we had for
[06:06] today is ghost records killing
[06:08] campaigns. from your expertise, why do
[06:11] you think most waterfall vendors fail?
[06:16] >> Yeah. So, what's going on right now is
[06:19] actually not many people have talked
[06:20] about this. I sort of broke this story a
[06:22] few weeks ago. What we're seeing is a
[06:25] lot of people are actually emailing
[06:28] catch all ghosts.
[06:31] Now, what I mean by that is
[06:34] essentially you you go on an email
[06:36] finder and I'm going to share my screen
[06:37] here. I just have to turn the video off
[06:39] for a second just to share it. But if
[06:41] you look at what's going on here, you
[06:43] guys can see my screen, correct?
[06:46] >> Yes, we do. J. Yeah.
[06:48] >> Okay, great. So, what we're seeing right
[06:51] now is there's this catchall ghost where
[06:55] a lot of providers out there are
[06:57] starting to talk about their guarantees
[06:59] on catchalls and all of that.
[07:01] Unfortunately, there's not a great way
[07:03] to verify if it's a proper email. Now, I
[07:07] want to talk about the word valid. Valid
[07:10] is is a very interesting word because
[07:12] it's it's very loosely organized. And if
[07:15] a domain is catchall, which means it
[07:17] accepts any email for any reason and it
[07:20] won't hard bounce, it becomes a lot
[07:22] harder to figure out if it's actually a
[07:25] valid email, right? There's a lot of
[07:27] difference. Now, an email also can be
[07:30] valid. And on top of that, what it what
[07:34] also can happen is there's a uh there
[07:37] there's a it's a valid email, but it's
[07:39] it's not really valid. And what I mean
[07:42] by that is
[07:44] uh you know, there's there might be an
[07:46] inbox there, but there's not a person
[07:49] there, which is an even weirder problem.
[07:51] So, email finding is going to get
[07:53] changed. I think we've disrupted it, of
[07:56] course. Uh we've had to and you know, we
[07:58] still have some area to uh grow a little
[08:00] bit. I know. Um, we're always looking
[08:02] for feedback and and you know the loop,
[08:04] but I want to just talk to you about a a
[08:06] typical waterfall enrichment here today
[08:09] of finding emails. It's critical. And
[08:12] listen, people will disagree with the
[08:14] strategy at some point. There's
[08:15] definitely a philosophy and and certain
[08:17] strategies here, but I want to talk
[08:19] about this. So, this is my email. We
[08:21] found it. All of the providers found it.
[08:25] Now what I want to talk about is uh a
[08:28] particular problem that I'm seeing right
[08:30] now where you essentially will go in and
[08:34] you will find a bunch of emails of
[08:38] people who used to there's a couple of
[08:41] problems. There's the used to problem
[08:44] which means they used to work at the
[08:46] company or
[08:48] they actually never work there and the
[08:50] vendor is pattern matching.
[08:52] Now, I want to talk about that in detail
[08:55] uh right now and I'm going to show you
[08:57] what I mean by that. So, I'll try to
[09:00] make this a little bit humorous, too. If
[09:02] you could if you could just go along
[09:03] with it, uh you'll see what I mean. But
[09:06] basically, if we're going to talk about
[09:07] a couple of companies, let's just talk
[09:09] about Glad Bees. Uh that's just a
[09:11] company people might cold email. They
[09:12] sell do some engineering work there. But
[09:15] let's try this one. Uh let's try uh
[09:19] George Washington who was the first
[09:22] president of the United States. He
[09:24] clearly does not work at CloudB as you
[09:27] know. And what we're going to do is
[09:30] we're going to say okay not there.
[09:31] Right. So we we have not located his
[09:35] email. It is not there. Find email did
[09:38] not find it. But what we're going to do
[09:40] is we're going to wait to see if the
[09:42] other vendors uh actually did find this
[09:45] email. Now, if they did, it could be a
[09:48] problem. Unless there is a George
[09:50] Washington that works at the company.
[09:53] So, let's take a look here under uh
[09:57] Sales Navigator just to make sure I'm
[09:58] not using an email that uh as you know
[10:01] could be um not real. Uh so, the last
[10:04] name would be George and the first name
[10:06] would be Washington. That would be a
[10:08] tough name for you know, you'd get
[10:10] compared a lot, but he doesn't work at
[10:12] the Let's see if he works at the White
[10:13] House. Maybe not. Uh, but let's just
[10:16] take a look here. Um, and by the way, we
[10:19] do have a match right now. Whiza has
[10:22] found George Washington's email.
[10:24] Apparently, he does work at the White
[10:26] House. And this is a very big problem
[10:28] because we all know he doesn't work
[10:30] there. Uh, or sorry, he did work there,
[10:32] but he's, God rest his soul, you know,
[10:34] he's not alive anymore, unfortunately.
[10:36] He was a great president, but um, but
[10:38] anyways, Cloud Beast. So, there's no
[10:40] George Washington there. Now we have now
[10:43] found him in two of the spots. So find
[10:46] email did not find him which is good.
[10:48] You the answer to this question is you
[10:50] would not want to.
[10:53] This is a big problem because what this
[10:55] tells you is they're willing to give you
[10:57] just about any email address. And what
[10:59] this is going to do is this is going to
[11:01] raise the cost of your waterfall
[11:03] significantly.
[11:06] Now the other problem that we're seeing
[11:09] challenges on is when people go and they
[11:11] start their list. Many people will start
[11:13] with a bulk list from Apollo or or one
[11:16] of those sources like sales navigator or
[11:19] whatever they're doing. And then what
[11:20] they'll do is they'll take that list.
[11:22] Now if that list is missing anybody or
[11:25] has a person who used to work there,
[11:28] let's take a look at that. That's
[11:29] another use case that we've seen uh
[11:32] starting to plague. So you really want
[11:34] to and the reason for this is I want to
[11:35] educate people. What you really want to
[11:36] do is you've got to check the employment
[11:38] of these people and this is a big
[11:41] problem right? So let's say they used to
[11:43] work there. So past company yes they
[11:46] used to work at cloud bees but their new
[11:48] company is not and obviously their name
[11:51] is not George Washington. This is
[11:52] another group of people I want to
[11:53] identify. So unfortunately what'll
[11:57] happen with this list is let's let's
[11:59] look up Katherine Lamb. Right? This is a
[12:02] good good example right now. When did
[12:05] Katherine work there? Katherine worked
[12:07] at Cloud Bees back in
[12:12] Okay. Wow. It was a while ago. So, 2020.
[12:17] >> Okay. So, Catherine worked there at in
[12:22] 2020.
[12:23] Uh, let's see where she works now.
[12:26] Obviously, she works at a different
[12:27] company,
[12:29] Lamb.
[12:31] And we will uh check uh test the test
[12:34] the waters here. Um no email found. Find
[12:39] email founder but she doesn't work there
[12:41] anymore and it's a valid email address.
[12:44] So let's see if the other two vendors
[12:47] they have to do a call back. I think
[12:48] they have a researcher go and run it. It
[12:50] takes a little bit of time but this is
[12:52] because what we're saying is they don't
[12:55] work at the company. They're not
[12:57] employed there. So if you pulled the
[12:58] data, we do have a thing that says
[13:00] employment verified. So what you want to
[13:02] do is if you're not using lead magic,
[13:05] which would be weird, but you would have
[13:06] something in the beginning of this that
[13:08] would say uh, you know, you would say,
[13:10] does the person work there? And you
[13:12] would want to look at, you know, some
[13:14] source of data where you would find out
[13:17] where people work. Of course, there's a
[13:19] couple of websites on the internet that
[13:20] tell you that. So you'd want to look at
[13:22] one of those sites and you'd want to do
[13:24] it with all the terms and conditions
[13:25] that those companies have and you know
[13:27] using their data for that and you know
[13:28] you want to look at that. So that's what
[13:30] you would do and you would do that with
[13:32] all that. So it's very important to know
[13:36] this. Now the problem in a waterfall
[13:38] Akos I'll go over to you. What do you
[13:40] think happens if this email says not
[13:42] found? Will it go to this one or not?
[13:44] >> It should essentially go to this one.
[13:46] Right.
[13:47] >> Right. So this won't be found. this will
[13:50] be found. Now, what you've just done is
[13:52] you've just Now, even if you said it
[13:54] wasn't found, that could be another
[13:56] situation.
[13:58] >> If you go there, you're going to go to
[14:01] here, you're going to spend the money,
[14:02] and then it's going to stop here.
[14:04] >> But unfortunately,
[14:06] what this will end up doing, and what's
[14:08] hard is it's the same status. So, it
[14:09] says valid. I prefer to say valid
[14:11] catchall, but that's the way life is
[14:14] sometimes. And if you say valid, that
[14:16] means you're going to email it. Now,
[14:18] what's going to happen when that
[14:19] happens? It's going to soft bounce,
[14:20] right? It's going to bounce internally.
[14:22] You're not going to see it.
[14:24] >> Now, what is the risk there? Well, I
[14:27] believe that Google and Microsoft are
[14:29] definitely looking at this very closely
[14:31] and they're looking at I call it the
[14:33] transferred inbox problem.
[14:34] >> So, you have a lot of employees. Now,
[14:36] look, when she worked there, we we we
[14:38] decided we saw that, right? So, this was
[14:40] a while ago, right? Yes.
[14:41] >> This was 2020. This is very old
[14:44] information. Mhm.
[14:46] >> So, the problem is you're going to run
[14:48] into this issue depending on how far
[14:50] down the waterfall you go. And this is
[14:52] why I like partnering with Clay because
[14:54] they're all about this and they're
[14:55] they're they're constantly getting the
[14:57] best data in here. But this is where the
[14:59] risk of of a long waterfall process
[15:01] comes in. So, you want to choose very
[15:03] wisely uh on these details. This is just
[15:06] kind of just illustrating the point.
[15:09] I'll take some questions, but this is
[15:10] sort of like pretty clear cut and dry,
[15:12] right? I think unfortunately if you put
[15:15] anything in here,
[15:18] some of them are going to
[15:20] um
[15:24] let's just see. I mean, I haven't tested
[15:26] this before. This is a brand new test.
[15:28] I've tested cloud bees because I know
[15:30] it's catchall. So, find email could
[15:32] probably still do that. So, that must
[15:34] mean that's in the database somewhere.
[15:36] >> Obviously, if it was in my database, it
[15:38] would have been eliminated because it
[15:39] would have been uh thrown out because
[15:40] they don't work there anymore. But um
[15:45] but let's see if the other two um find
[15:48] it. This is a good test.
[15:51] And this is how we tested uh waterfall
[15:54] systems basically just to see like do we
[15:56] continue down the path if that makes
[15:58] sense.
[16:00] So go ahead. I'll I'll pause there if
[16:01] there are any questions sort of. That's
[16:03] a good spot to stop there.
[16:04] >> Absolutely. We're picking up one from
[16:05] the chat. Jesse, any thoughts about
[16:08] catch all verifiers like Scrubby?
[16:12] >> Ah, good question. Yeah, so Scrub is
[16:14] good with um it's it's a good way to do
[16:16] it. Uh the only problem is it's hard to
[16:19] detect sometimes if something So Scrub
[16:22] is looking for bounces, right? They're
[16:24] looking for hard bounces, right? They're
[16:25] going to the way that they do it. Uh and
[16:27] Nick's a close friend of mine. I like
[16:29] Nick a lot. He's a he's one of the best
[16:30] out there. They're going to detect if
[16:32] it's a hard bounce, which will hurt you
[16:33] more for sure. But here's the paradox
[16:36] that you're in is is um one of the
[16:40] problems with these emails now is
[16:42] remember even though it doesn't hard
[16:43] bounce it doesn't mean that Google and
[16:45] Microsoft don't have the information and
[16:47] that's primarily you're emailing Google
[16:49] and Microsoft you know uh service uh
[16:52] accounts right so unfortunately the data
[16:55] is still there in the system and we
[16:57] don't nobody actually knows the
[16:59] behavioral patterns that they're looking
[17:01] for for spam filters so obviously if you
[17:03] want to land in the primary. You got to
[17:05] be very careful there, right? I'm not
[17:07] saying I think Scrub is good to find the
[17:09] hard bounces, but it's not going to find
[17:11] like it's not going to find the soft the
[17:13] soft soft bounces. These are ones where
[17:16] the email address might exist like when
[17:18] I if I have an employee at the company
[17:20] that we transition to a new inbox,
[17:22] what's going to end up happening is that
[17:24] person's going to go take another inbox
[17:25] somewhere and it's going to get
[17:27] transferred to their manager. Now, is it
[17:29] likely that Catherine's new manager is
[17:32] responding to cold emails? Probably not,
[17:34] right? I I would imagine. Or the new
[17:36] manager at CloudB that runs this role.
[17:40] >> She's already here. I mean, she's
[17:41] already had four jobs, five jobs, you
[17:44] know, like that's the problem right now.
[17:46] You got to watch out for. Now,
[17:49] >> I'll get in my support chat and there'll
[17:50] be people that say, "Hey, you're" and
[17:53] and very rarely does this actually
[17:54] happen. Usually we're about the same
[17:56] coverage, but we'll have somebody
[17:57] complain that, hey, this tool had a
[17:59] better coverage. And I said, well,
[18:02] sometimes there's not much you can do
[18:03] about that. And downside is the way that
[18:06] I get incentivized to find you emails is
[18:08] not by finding no. When I send back that
[18:11] to Clay, I don't make any money. I lose
[18:14] money, right? Like or actually, I don't
[18:17] lose money. I should have never received
[18:18] money because I didn't give you an email
[18:19] address.
[18:20] >> True.
[18:21] >> It still costs money to give you nothing
[18:23] back, right? because I had to check and
[18:25] I had to real I do a real time check so
[18:27] if somebody leaves the job we're pretty
[18:29] close like we're within a month or two
[18:30] of everybody. Um you just got to you
[18:32] know there's logistics there and we're
[18:34] doing it in real time which is another
[18:35] thing that you got to really start to
[18:37] look at. This is why you got to be
[18:38] careful if these vendors start to cash
[18:41] the data, right? They cash it because it
[18:44] costs them less to make a network call
[18:47] to a a caching layer than it does a
[18:49] network call to a service that would
[18:51] tell you if it if it's an actual
[18:53] employee or not. So that's sort of
[18:56] what's going on. Uh you know this is
[18:58] this is the way it is. Now, one other
[19:01] quick thing. There are these situations
[19:04] here where some of the vendors what they
[19:07] do is they have this like catchall email
[19:09] result and if you turn that on they'll
[19:13] find everything. That is a risky move
[19:15] too.
[19:15] >> Absolutely right.
[19:19] >> You see what I mean?
[19:20] >> Yep. Yep. Yep. Damn.
[19:26] This is bad.
[19:28] And Jesse, would you also mind zooming
[19:29] in your screen?
[19:30] >> So, this is where the risk is. If you're
[19:31] building a waterfall, you got to be very
[19:33] careful how you do these waterfalls
[19:35] right now. And what I'm telling you is
[19:37] in the back of the waterfall, the most
[19:39] opportunity exists to give you bad
[19:41] emails.
[19:43] >> True.
[19:45] >> And I'm not Look, I don't think they're
[19:46] I'm not I would never say that any of
[19:48] these vendors are doing this
[19:49] intentionally. I I'm not I don't think
[19:52] that's the truth. I I wouldn't and and
[19:54] they they wouldn't tell you that either,
[19:55] I bet. Uh, and Clay, I've talked to Clay
[19:58] about this. Obviously, Clay is um all
[20:00] about like making sure they're they got
[20:02] the highest quality. And by the way,
[20:04] this is rampant and very rampant in some
[20:06] of the other bigger providers. I'm not
[20:08] going to name names, but what's good
[20:10] about this is this gives a lot of
[20:12] people, this is why I've disrupted this
[20:14] space pretty pretty brutally here,
[20:16] right? This this is a very very very big
[20:18] illustration of how this is going. And
[20:22] um you know, you got to be super careful
[20:24] and you got to use the highest quality
[20:26] and you got to do the testing yourself
[20:28] actually. You can't really trust
[20:30] everybody to do it. And I and listen, if
[20:32] you find things wrong with us, we're
[20:34] really open to feedback. We will uh so
[20:36] we don't do a catchall guarantee because
[20:39] I think that's a slimy kind of thing to
[20:41] do anyways, right?
[20:42] >> But we will take the request feedback
[20:45] and we'll go and make changes to our
[20:46] algorithms and things like that. I I
[20:48] don't think, by the way, I don't think
[20:49] any of these vendors will actually pay
[20:51] you on that anyways. I think that's a
[20:53] complete lie. Anyways, but um you know
[20:55] what I mean? That that's something that
[20:56] I see people talking about. But who's
[20:58] going to go refund 10 cents worth of
[20:59] email finding? I mean, that's a little
[21:01] weird too if you ask me, but stop there.
[21:04] >> Absolutely. So, picking one more
[21:06] question from the chat, Jesse. Would a
[21:08] pessimistic waterfall approach be the
[21:10] way to go then? That is if one of them
[21:12] fails, it's a bad lead.
[21:16] >> Yeah. Um, you know, I'm going to pass on
[21:21] say that is because it starts with the
[21:23] assumption that every email is good that
[21:27] they give you. Um,
[21:31] it's a tough question. I I I want to
[21:33] pass on it though because I'm very
[21:35] biased on it and I can't answer it
[21:38] without being super biased because of
[21:40] how much experience I've had. I mean, I
[21:41] ran a cold email agency. It was very
[21:44] been a very successful cold email agency
[21:45] before we became a SAS company. Uh, you
[21:49] know, it's it's just a hard cell to for
[21:51] me to it wouldn't be fair if I answered
[21:53] it. I think I would rather people since
[21:55] I'm directly competing in this waterfall
[21:58] process. It's a it's it's a really
[22:00] tough, you know, part to for me to be
[22:03] honest on. I mean, I have an opinion,
[22:04] but it's not it's a pretty good, you
[22:07] know, it's it's I tested a lot of data
[22:09] and facts, and you know, we just found
[22:11] what we found. And listen, this is why
[22:14] you got to be very knowledgeable. You
[22:16] got to try to keep these costs in check
[22:18] because, you know, if you did this
[22:20] waterfall here, right, you would have
[22:21] spent I mean, the right answer to this
[22:24] question would be, do you want to email
[22:28] people who don't work at the company
[22:29] anymore? I would say no. That would be
[22:32] my preference. I know I've talked to
[22:33] people and they say yes, I would want to
[22:35] email them.
[22:37] >> And I don't know why because I don't
[22:39] think their new manager is gonna answer.
[22:41] I mean, that's probably not.
[22:43] >> But I've argued, by the way, I've had an
[22:45] argument with somebody on this and I
[22:47] think they were just defending their own
[22:48] company. But I was like, listen, there's
[22:50] a point where you just say like, you
[22:52] know, rock beats paper or or sorry,
[22:55] paper beats rock, you know, scissors,
[22:57] you know, the whole thing here. Rock,
[22:58] paper, scissors. But
[23:00] >> eventually you just say, "Yeah, I lost.
[23:02] I got to go find another way to do this.
[23:04] And you can't give email addresses that
[23:06] are 2020.
[23:07] >> Absolutely.
[23:08] >> And that's the value, right? I mean,
[23:11] >> 100%. 100%. And picking one from the
[23:14] chat again, Jesse. What are the benefits
[23:16] of waterfall if you're providing most
[23:18] likely emails?
[23:21] >> So, when you say most likely, um, I'll
[23:25] just assume what you're talking about is
[23:26] the valid catchalls. Is that the one?
[23:29] >> I assume the same. Mark, correct? If
[23:31] you're wrong, uh, drop it in the chat
[23:33] and we'll revise.
[23:35] >> I'm just not I'm not following the
[23:37] question. Uh, most probably I'm not
[23:39] sure. I'm not if I just want to make
[23:40] sure I understand it because this is
[23:42] getting really uh detailed in the data.
[23:44] So like if somebody could just be a
[23:47] little bit more I think it'd be a little
[23:48] more specific there. I would like to um
[23:50] understand the question a little bit
[23:51] better just before I answer it.
[23:53] >> Right. So what are the benefits of
[23:54] waterfall? If you're providing most
[23:56] likely real emails basically means real
[23:59] people, real email addresses as opposed
[24:01] to catchalls.
[24:06] >> Um, yeah. So, this is the tricky
[24:08] question. So, catch all emails are going
[24:11] to probably come from a database
[24:12] somewhere. Uh, or they're going to come
[24:14] from a couple of other methods that are
[24:17] out there.
[24:19] Uh none of the catchall methods are
[24:23] well yeah so you have to be a little bit
[24:27] careful how you so it depends and
[24:30] vendors are going to be likely not talk
[24:33] much about this uh area because of some
[24:36] of the um strategies involved here. So,
[24:40] you know, they're going to be a little
[24:41] bit, you know, they're not, you know, if
[24:43] you asked, "How do you guys find catch
[24:44] all emails?" They're going to tell you,
[24:46] "Well, we use a lot of heruristics data,
[24:48] blah, blah, blah, blah, blah." They're
[24:50] not going to really totally get into it
[24:51] because of, uh, there's a couple of
[24:53] methods you can use. Uh, one of the
[24:55] methods, which we don't use, um, per we
[24:58] don't use it because I think it's a bad
[24:59] method. You know, what some people have
[25:01] done is they'll do like a forgot
[25:03] password, but that that would be a bad
[25:04] idea. I think that's a really bad one.
[25:06] um you know, you you would get a
[25:08] different response from somebody who has
[25:09] an inbox versus somebody who doesn't. Uh
[25:12] but I wouldn't use that. I think that
[25:13] would be it would also violate all the
[25:15] terms and conditions of the platform and
[25:18] it would also send people you're about
[25:19] ready to email a forgot password and
[25:21] you'd have security probably problems
[25:23] there. You probably get banned from the
[25:24] platforms you're using to do that. So,
[25:26] I'm sure it's a violation of their terms
[25:28] and you know, you got to be careful
[25:29] there. You shouldn't really use that
[25:30] method. um other methods out there. I
[25:34] don't want to get into like all the
[25:35] strategies, but um just because like
[25:37] there's some areas there, but I mean
[25:39] that's really what the conversation goes
[25:40] to. So, it's a hard discussion to have
[25:43] there.
[25:43] >> Got the answer, Jesse. Got the answer.
[25:46] Picking up one more question from
[25:47] Joshua. Does the lead magic data pool
[25:49] include its own internal waterfall where
[25:52] leads are cross referenced with external
[25:54] sources when leads are pulled?
[25:57] So, we have our own sources, but I'm not
[25:58] calling uh I wouldn't I wouldn't call
[26:01] any of the the vendors in the the
[26:02] current none of the I I don't have any
[26:05] uh vendors that are here, right? Uh like
[26:08] my methods are more around like
[26:11] uh
[26:13] you know um does the person work at the
[26:16] company or not, right? That's a big
[26:18] question. And there's a lot of different
[26:20] ways to
[26:22] make a phone call to the company and
[26:24] ask. Um, that's one way to do it. Um,
[26:26] there's there's other ways to do it. You
[26:27] could have Ivy League College interns
[26:29] calling it. That's another method you
[26:31] way you could do it. You could call have
[26:32] them call the front desk and say, "Hey,
[26:34] do you guys does this person work
[26:36] there?" And, you know, maybe they're
[26:38] maybe they can't tell you that. Maybe
[26:39] they can. I don't There's a lot of ways
[26:41] to do it. Uh, we're doing it in real
[26:42] time. We've actually developed a way to
[26:45] do that in real time, so we know how to
[26:46] do it. But there's a lot of ways to do
[26:47] it. Uh obviously you'd have to kind of
[26:49] play within the rules there. So um we
[26:51] would obviously play within the rules
[26:53] all the time. So that that'd be the way
[26:54] to do it.
[26:56] >> Understood. Last question on the chat.
[26:59] It's from Brandon. I recently ran a list
[27:01] through Lead Magic then ran the catch
[27:03] alls through another provider who
[27:04] claimed to verify catchalls. Did I do
[27:07] that backwards?
[27:11] >> Oh um let's think. So verify the
[27:16] catchall. So, so the question is is like
[27:19] were you verifying the email that we
[27:21] gave you and then so here here's the
[27:24] weird thing about the catchall
[27:25] verification tools. Some of them are
[27:27] giving you the catchalls and they're
[27:30] right. They're like, "Yeah, that email
[27:32] exists. That email inbox exists." So,
[27:35] there's a couple methods where it will
[27:37] tell you that the email inbox exists.
[27:42] >> But remember, there's another problem
[27:44] there, and I just exposed it. This is
[27:47] where I've really just because I was
[27:49] getting into a lot of these tool
[27:51] discussions of like you know I was the
[27:53] ones that would come up the usual
[27:54] suspect would be like bounce span and
[27:57] those ones right and it be like well
[27:58] they got a catch all verification like
[28:00] well okay well let's talk about that I
[28:02] mean there's a couple ways to do it I
[28:04] don't really know how they're doing it
[28:05] I've played around with it I've looked
[28:07] to see how they're doing it and have a
[28:08] good idea how they're doing it although
[28:10] the problem really lies in the fact that
[28:12] there you know where where it becomes a
[28:15] little bit of a problem.
[28:17] >> Mhm.
[28:18] >> Uh is the catch all emails that will
[28:22] verify on the catchall method
[28:26] but won't
[28:28] uh they don't work there. So, it's
[28:31] likely Catherine's inbox is still there
[28:35] and would verify.
[28:38] >> Right.
[28:39] >> You could probably guess her I would
[28:40] guess if I had to guess I bet her email
[28:44] was that. I would guess that that's
[28:46] correct.
[28:46] >> Absolutely. I would have done that too
[28:48] until you told me
[28:52] >> uh you know if you went into bounce
[28:55] there's a few out there. But like here's
[28:57] the issue is like if you checked to see
[29:00] and I'm just checking like you know
[29:01] there's a lot of ways we would never use
[29:03] LinkedIn to check this ever for any
[29:06] reason. There's just no real reason to
[29:07] do that. Um because you have a lot to
[29:09] deal with, right? LinkedIn does not
[29:10] allow that and that we would never use
[29:12] LinkedIn to do that. But you could use
[29:16] LinkedIn if you wanted to just do it
[29:17] from a research perspective. That would
[29:19] be completely obviously above board in
[29:21] terms and services. But if you were to
[29:23] go into Bounceman and you were to check,
[29:26] I I don't know what they would say. I
[29:27] mean, we're doing a live show here, so I
[29:29] have no idea the answer to this question
[29:30] before I do it. So, they're saying it's
[29:32] deliverable. So, that means that you
[29:33] could get an email here. Now, the
[29:35] problem is that's the problem, right? is
[29:38] it is the right email address probably
[29:40] for Katherine at one point but the
[29:42] problem is she doesn't work there
[29:44] anymore so doesn't really matter you're
[29:46] not going to get her
[29:48] >> true
[29:49] >> I just got sick of it because we were
[29:51] getting a lot of these questions and and
[29:53] I started to see a lot of people that
[29:55] were just like coming at us like hey you
[29:56] know do you do catch all I'm like
[29:59] we do everything right like we're not
[30:01] you know we're going to give you the
[30:02] right email addresses but if if I got to
[30:05] tell you we're doing a catchall
[30:06] verification it's It's just annoying
[30:08] even talking about the word catchall,
[30:09] right? We're going to, you know, and
[30:11] this is where I think we've really
[30:12] disrupted the market because
[30:15] >> yeah, catchall, but if the person
[30:16] doesn't work there, who what are you
[30:18] emailing? Now, there is one other method
[30:20] that I find to be a little bit Let me
[30:22] see if I can trigger it. There's one
[30:23] other company that does something
[30:24] interesting.
[30:25] >> I don't really uh I've gone back and
[30:27] forth on this. I don't like how they're
[30:29] doing it. Um, but it's probably better
[30:33] than nothing, but it might not be better
[30:34] than nothing. Actually, it might be
[30:35] worse.
[30:37] And what I mean by that is ICP sometimes
[30:40] will give you the new email, but I don't
[30:41] think the new email is very helpful
[30:43] actually,
[30:44] >> right?
[30:46] >> And they do it sometimes, and a lot of
[30:47] the times they're wrong, but uh Oh,
[30:49] nope. This one they're saying they're
[30:51] ultra sure that it's ultra sure. I have
[30:53] no idea what the hell that means, but uh
[30:56] cloud bees. Yeah. So, like I don't know.
[30:59] I mean, that's tricky, but
[31:02] I don't know. Um,
[31:05] yeah. I don't know what that means, but
[31:07] sometimes they'll trigger and they'll
[31:08] give you the new email address, but I
[31:10] don't think the new email address is
[31:12] helpful either. I think that's actually
[31:14] just as risky. Uh, to be honest with
[31:16] you, I actually think that's weird, too.
[31:18] Imagine if you're just emailing a list
[31:19] and all of a sudden you're emailing like
[31:20] a person at a new role. It's like, hey,
[31:22] I saw you were at Cloud Beast three
[31:24] years ago, five years ago. Like, that's
[31:26] a weird I don't really know what the
[31:28] purpose of that is.
[31:29] >> It makes sense. Yeah. You know, like
[31:34] So yeah, I mean, look, I I don't want to
[31:36] disrupt the market too bad, which I knew
[31:38] what I was going to do when I did this,
[31:39] but we're going to do it anyways. It
[31:41] doesn't really matter. So that's why I
[31:43] did it. And, you know, it's just it is
[31:44] what it is. I mean, we had to do
[31:45] something, right? We're we're
[31:47] competitive. We we believe in, you know,
[31:49] a competitive business environment. And
[31:51] that's what this is. This is a very
[31:52] competitive business environment. Now, I
[31:54] don't think these companies are doing
[31:55] anything malicious. I think if they knew
[31:56] about this problem, they would probably
[31:58] fix it. Hopefully, that would be the
[31:59] right thing to do. But I mean, look, the
[32:02] problem is you just spent if you if you
[32:04] factored this in, you spent four, you
[32:06] know, if you did clay credits, let's say
[32:08] that's 4 cents, that's 8 cents, and you
[32:11] got a a little bit of a problem here,
[32:12] and you've now nicked your domain
[32:13] because you've triggered that, you've
[32:14] emailed a transferred inbox.
[32:16] >> Yes,
[32:17] >> you got to be very careful on these
[32:18] transferred inboxes, right? These are
[32:20] the ones that they're going to detect
[32:22] right now. And I bet a lot of you are
[32:23] emailing these. I actually talked so I I
[32:26] talked to Eric uh Eric Doski and uh Nick
[32:29] Abram and both of them you know told me
[32:32] that they are emailing a lot of these
[32:34] now
[32:35] >> right
[32:35] >> so they're they're they're obvious
[32:37] they're they're using lead magic now and
[32:39] and everything. So you know we we
[32:41] generally are going to be better
[32:43] expecting probably like like a a pretty
[32:46] good detection here where obviously
[32:47] we're improving it. Um it's not 100% but
[32:49] it's it's pretty pretty damn close to
[32:51] detecting on all these things. But the
[32:53] problem is if you keep the keep the drip
[32:55] on and you keep going down the the the
[32:57] wire, you're going to get a lot more
[32:59] results, but the results aren't going to
[33:01] be necessarily good. That's the problem.
[33:02] >> Absolutely. What exactly saw a couple of
[33:04] minutes back, right? You go down the
[33:06] line, you get some results, but that's
[33:07] not what you need. Ghost records.
[33:10] >> Results aren't always good. You need
[33:12] good results. That needs to be
[33:14] >> You got to be careful here. I mean, we
[33:16] got a little bit of You got a little bit
[33:17] of a problem. I think we just disrupted
[33:19] the whole waterfall to be honest with
[33:20] you. I think the waterfall just got
[33:22] disrupted a bit here um on this
[33:24] discussion
[33:25] >> right in the meantime picking one more
[33:28] from the chat Jesse. So whether a person
[33:30] is currently working at a company or not
[33:32] is something that is built into each
[33:34] lead magic when
[33:37] I'll go for it again. So whether a
[33:38] person is currently working at a company
[33:40] or not is something that is built into
[33:42] each lead magic lead when pulled.
[33:45] >> It's a check. Yep. It's a check we do.
[33:47] Now here's the thing. I'm going to tell
[33:48] you the check isn't 100% accurate. It's
[33:51] really close. So, it's gonna get rid of
[33:53] about 99% of them. But, there are going
[33:55] to be some you're going to find where
[33:57] they don't because of some of the way
[33:58] that it works. Uh, you're going to have
[34:00] obviously like I I I actually did it,
[34:02] and this is one you could argue. I
[34:04] actually did it on a list of a thousand
[34:05] that every one of these vendors got
[34:07] wrong,
[34:08] >> right?
[34:09] >> And uh
[34:11] we found one of them, one of the wrong
[34:14] ones, and it was an intern,
[34:16] >> right? who who who um changed jobs that
[34:20] month. So, they changed in August.
[34:23] >> Wow.
[34:25] >> So, you know, that's like the thing is
[34:27] like I might still email that person if
[34:29] they left the job in August. It might
[34:31] actually make sense.
[34:32] >> Fair enough. And I think
[34:34] >> I don't know. There's like right and
[34:36] wrong is all like right and wrong is all
[34:39] like what is right to you more or less.
[34:42] So, you kind of have to test this a
[34:43] little bit. I hate to like leave it this
[34:45] vague and this like weird, but honestly,
[34:48] I'm just trying to get everybody to go
[34:50] out there, try to figure this process
[34:52] out.
[34:53] >> It's going to really matter, right?
[34:54] Like, this is the stuff that you're
[34:56] going to want to really consider as
[34:58] you're building this process out. And I
[35:00] don't think there's anybody in the
[35:01] market. I've looked around. I cannot
[35:03] find a single person in the market who's
[35:05] been talking about this except for me.
[35:07] >> Yeah, 100%.
[35:09] I'm the example. If if I didn't know
[35:10] this, I would have going through the
[35:11] waterfall and I would have sent emails
[35:13] to those leads. Jesse, but yeah, as you
[35:15] said, it's I think it's for us to kind
[35:16] of uh you know, you put it out here. You
[35:18] put out what you found and it's just
[35:19] it's for us to kind of go experiment,
[35:21] see what's working and what's not
[35:23] working. Absolutely.
[35:24] >> This is risky for me, too. I'm going to
[35:26] be honest. This is very risky. What the
[35:28] easy way, the easy path for me to do,
[35:29] I'm number, by the way, I'm number one
[35:30] in their waterfall, right? The easy path
[35:32] for me would have been to do this.
[35:36] >> Absolutely. And and and it looks
[35:38] welcoming, right? It wants you to kind
[35:39] of email it from a perspective, but
[35:43] >> makes sense. And the floor is open for
[35:45] questions as well, folks. If you have
[35:46] any questions, turn on your videos,
[35:48] raise your hand. I'll spotlight you. You
[35:50] can shoot your questions directly to
[35:51] Jesse and he'll get them answered for
[35:53] you.
[35:56] And in the meantime, how does the lead
[35:57] magic find open jobs for a company work?
[36:00] Pull from website, LinkedIn, glass door?
[36:03] >> Corporate corporate job board only.
[36:08] You're talking about our job finder,
[36:09] right? Corporate job boards.
[36:13] >> We got a We got We got a bite. I always
[36:15] love it when there's a bite on.
[36:17] >> I love I love watching this because it's
[36:19] just like, are they going to do it? Oh,
[36:21] don't do it. Don't do it. Oh, they did
[36:23] it. Such a sucker move.
[36:28] Oh god.
[36:33] >> I think we all are currently focused
[36:34] onto that. There's two minutes of mute.
[36:38] But yeah, one question from Brandon as
[36:39] well. U what
[36:44] what are corporate job boards and how do
[36:47] you verify if the person still works
[36:48] there?
[36:51] >> Uh we we check sources that tell us if
[36:54] they work there. There's a lot of ways
[36:55] to do it. You could call the front desk.
[36:56] You could do it. You just have to do it
[36:58] really quickly if you're doing it live.
[37:00] Uh there's a lot of ways to do it. Um,
[37:02] there's a lot of websites that you could
[37:03] verify if the person worked there or
[37:05] not. Uh, I don't want to go into like
[37:07] all the details there. There's there's
[37:09] several different websites that you
[37:10] could check to see. Uh, you know,
[37:13] there's there's just a lot there. I
[37:15] don't want to like directly, you know,
[37:17] there's no reason to to go through like
[37:19] each individual API call. Every one of
[37:22] them is going to be different. So, um,
[37:24] you know, I just want to make sure I'm
[37:25] kind of clear there.
[37:27] >> Absolutely. And folks, I think if you
[37:29] have any questions, you can turn on your
[37:31] video or unmute yourself, shoot your
[37:32] questions, and we'll get them answered
[37:34] for you.
[37:36] Anything? Any questions?
[37:49] It's one of these things that like you
[37:51] watch this webinar back and it might go
[37:53] shorter than normal, but it's one of
[37:55] these things where everyone's sort of
[37:56] like when I walked so I'll give you an
[37:59] example. I walked Eric who I think is
[38:01] probably one of the most knowledgeable
[38:02] people in cold email. I walked him
[38:04] through this problem and he
[38:08] he goes, "Let me call you back." He
[38:11] couldn't really like it was sort of like
[38:13] like a really weird moment of you know
[38:16] it was just like a weird uh I wish I
[38:18] could explain to you like the the the
[38:20] the feeling that you know he want he
[38:22] wanted to respond he's like yeah this is
[38:24] very in you know most people have
[38:25] responded very insightful but it's also
[38:27] like if they're if they're one of the
[38:30] top people in the world at cold email
[38:31] right this is like a new this isn't and
[38:34] I'm breaking this by the way this is
[38:35] broken I haven't broke this on any other
[38:39] uh webinar I haven't talked about this.
[38:41] I've talked about it in my own group
[38:42] called the SAS Yacht Club, but I have
[38:44] not talked about this on any other uh
[38:46] webinar. And obviously, I get asked to
[38:48] be on a lot of these email webinars and
[38:50] I I chose Smart Lead because I find them
[38:52] the users to be the most uh you know,
[38:55] knowledgeable and really care about
[38:57] email delivery and their clients like
[38:58] their agencies are always the most
[39:00] successful I found. And you know, like
[39:02] that's why I'm on Smart Leads webinar
[39:04] talking about it and I I told V I would
[39:06] do it of course as a favor and uh that's
[39:08] why I'm here. Obviously, it's like a
[39:10] it's a tricky situation. I don't I don't
[39:12] really know the answer to be honest with
[39:14] you. I don't have a great I I sort of
[39:15] found it and I was like, "Huh, this is
[39:17] weird and people need to know about it."
[39:19] Yeah, it just unlocked this part of
[39:21] brain for me cuz this isn't this is
[39:23] something new as you promised.
[39:25] >> And two more questions from the chat. As
[39:28] long as we validate all emails with lead
[39:30] magic, it won't end up in our final
[39:32] columns right?
[39:36] Uh, so that you don't need to do the
[39:38] validation stuff with lead magic if you
[39:40] if you did the email finder. That's
[39:42] something that people have asked me as
[39:43] much as I'd love for you to you know.
[39:45] No, you don't you don't need to do it.
[39:47] Um, we so it's very hard to do what we
[39:51] have to do to do to do I'll give you the
[39:53] like technology behind lead magic's
[39:55] email verification. So we obviously
[39:57] verification is a step and when I talk
[39:59] about verification I'm not getting into
[40:00] the find email like does it is it valid
[40:02] or not stuff. I'm talking about like a
[40:03] network verification, right? There's
[40:05] only one type of verification, right?
[40:07] It's like network verification. You send
[40:09] a
[40:10] >> you send a message. We are doing that
[40:13] >> at the very end no matter what. And I've
[40:15] told our engineering we we of course we
[40:17] have a slip or two here and there, but
[40:18] not like on the verification step. If it
[40:21] does not verify at the end as an talking
[40:24] about like if it comes back invalid, we
[40:27] are not sending it to you.
[40:31] >> Understood. like there's just no way
[40:33] you're going to get it back. It now we
[40:35] we could make a mistake. There could be
[40:37] a grreyless problem. Very unlikely
[40:39] though cuz we're we're we're spinning a
[40:42] lot of network calls out there and we're
[40:44] watching if we detect
[40:47] now catch all emails are a problem
[40:49] because you can't you can but it takes
[40:53] longer. I don't want to get into all the
[40:55] logistics of a network call verification
[40:58] on a catchall. that's a different game.
[41:02] Uh, and then there's other methods to
[41:04] use. And I know there's a couple of
[41:05] these vendors out there that think that
[41:06] we don't know what we're doing with with
[41:08] catch all verification. I laugh because
[41:10] I'm like, dude, we know it way better
[41:11] than you do, right? Like, you know, if
[41:13] you want to go and talk about it, I'll
[41:15] talk about it all day. And they'll
[41:17] they'll be humbled pretty quickly. So,
[41:20] uh, you know, but when we're talking
[41:21] about like a network verification at the
[41:23] very end of it,
[41:24] >> Mhm.
[41:25] >> we won't obviously know what's going on
[41:27] there and and and we don't let those
[41:30] out. Those are that would be a bug in
[41:32] our software. We'd want to know about it
[41:33] and we want somebody to report it, then
[41:35] we would fix it.
[41:36] >> Got it. Got it. And one question, Mark
[41:40] has raised his hand. There you go, Mark.
[41:43] Can you unmute yourself and go for it?
[41:47] >> What's that?
[41:48] No. Uh, there's a person from the
[41:51] audience asking a question. Um,
[41:52] >> can you hear me? Okay.
[41:53] >> Yep. Loud and g.
[41:55] >> So, I'm pretty new to all this, so
[41:57] excuse the uh stupid questions that that
[42:00] might come your way.
[42:03] >> So, I mean, I get that you're trying to
[42:06] position as like, you know, a superior
[42:08] um, you know, uh, email finder. My
[42:12] question is,
[42:13] and that totally makes sense to me, but
[42:15] what what's the use of a waterfall in
[42:17] that case? Like if you're saying, "No,
[42:19] there's no email found."
[42:21] Why would I want to then verify through
[42:24] someone else to find that email when the
[42:25] reason that you didn't find the email is
[42:27] because there's no valid email?
[42:30] >> Good, good question. This is a very good
[42:32] question actually. This is this is this
[42:35] is a very good question actually. Uh so
[42:37] I I I'm not working with any other
[42:39] vendors on this. Um but I am working
[42:41] with Clay. Clay is talking about adding
[42:44] a step to fix this to sort of like
[42:51] part of it is is we could tell you on
[42:53] the API don't go further. you would have
[42:57] to blindly trust us there or you would
[43:00] have to put the the proof of the and
[43:02] you'd have to test the person works like
[43:05] I so what I'm going to possibly be doing
[43:06] is saying the person works at this
[43:08] company now
[43:10] basically that'll be in the product soon
[43:13] uh I I have it finished today I just
[43:16] have to wait we have to get it into the
[43:17] waterfall as you know there's probably
[43:19] you know
[43:21] there's probably a lot of API calls
[43:23] being made so we have to like there's a
[43:25] little bit of a testing period you got
[43:26] to go through to get these things sort
[43:28] of integrated. But it's to come and I
[43:30] think what it'll do is it'll this will
[43:32] really differentiate everybody out
[43:34] there. You can use there's some
[43:36] technologies in clay that you could use
[43:38] today to sort of help your story there a
[43:41] little bit. But we're we're going to be
[43:44] even more disrupt. I'm not I'm not
[43:46] worried about even sharing. Like a lot
[43:47] of people like why are you even sharing
[43:48] that you're going to do this? Well, I'll
[43:49] tell you why. Because we can do it lower
[43:51] cost than anybody. So we don't care. So,
[43:53] we're going to, you know, we'll we'll be
[43:55] able to do it lower than anybody, so it
[43:56] doesn't matter. I'm not worried about
[43:58] the like risk. Uh, and I I run a lean
[44:00] team here, as you know, and um we we we
[44:03] pride ourselves on being like the
[44:05] highest quality and lowest cost. So, I
[44:07] mean, you know, it's like sort of it's
[44:10] something there. But like you're right,
[44:11] you really should have an abort button
[44:13] here where what what the ideal waterfall
[44:17] would be and this is the breakthrough
[44:18] moment here for most people is going to
[44:20] be if you had a column here that tested
[44:22] employment
[44:24] before they entered into this because
[44:26] this costs this is like an engineering
[44:29] escape.
[44:30] Fortunately, you can get that value
[44:33] here. And if we put not found, you can't
[44:35] I can't enhance this view yet, which I
[44:38] will be able to soon. That's the goal is
[44:41] to enhance this with hey, you didn't
[44:43] find we didn't we didn't find the person
[44:45] works there cuz I know this email used
[44:48] to exist or might still exist. I just
[44:50] don't want to give it to you because I
[44:51] know the person doesn't work there.
[44:56] >> Understood.
[44:57] >> Does that make sense?
[44:58] >> It does. It does. It makes a lot of
[45:00] sense. And uh one more question from the
[45:02] chat.
[45:03] >> This is not even a hard like for anybody
[45:05] explaining this. It's like not a hard
[45:07] concept to understand. It's very cut and
[45:10] dry black and white. That's why it's
[45:12] actually pretty good in terms of
[45:13] discussion.
[45:14] >> 100%
[45:15] >> and disrupt. We've disrupted a big big
[45:18] group of people on this. And um we were
[45:20] 13th place on the waterfall. Now we're
[45:23] number one. And then we had a chance to
[45:26] go and give a lot more email addresses,
[45:28] but we decided not to. Our goal was to
[45:31] give people higher quality email
[45:32] addresses as you know and that's what
[45:33] we're we're always aiming for. So we
[45:35] want to do that but we also want to like
[45:37] help you understand this. So you're
[45:39] gonna want to think about this. Send
[45:41] this out to people this video. Get this
[45:43] to your team immediately. Uh and if you
[45:46] find issues with ours, please let us
[45:48] know. We want to actually fix them. I
[45:51] I'm not like going to sit here and say
[45:52] I'm going to give you a refund or all
[45:54] the By the way, if you need the two
[45:56] cents back like okay, we'll talk about
[45:57] it. I can probably do it if we miss one
[45:59] or two. But like let's talk about the
[46:01] real problem here. Let's get this thing
[46:03] tied up. Like we're watching this pretty
[46:05] closely right now. Uh a lot of the
[46:08] vendors like Finding Mel and some of the
[46:09] other ones are doing these guarantees
[46:11] and I don't know anybody who's ever
[46:12] collected on these guarantees before. I
[46:13] think it's a weird kind of a weird, you
[46:15] know, it's like I only paid a half penny
[46:17] for the thing. You know, you should just
[46:20] fix it.
[46:23] >> 100%.
[46:24] >> Yeah. Thank Thank you. So, thank you so
[46:25] much for answering that. I guess I guess
[46:27] my essential you know question is like
[46:29] when you when you don't when you don't
[46:31] return an email like i.e. when you don't
[46:33] find the email and then it goes through
[46:34] the waterfall process there's two
[46:36] possibilities. One is that you can't
[46:38] find it. You don't have the capacity.
[46:40] The other is you looked and it's not a
[46:42] valid email.
[46:43] >> There you go.
[46:44] >> So that seems like a pretty critical
[46:46] difference.
[46:47] >> Yeah. Yeah.
[46:51] Thank you so much Clay. You could
[46:53] actually build this new waterfall in
[46:55] your system. Now, if you had somebody
[46:58] who was really good on automation, you
[47:00] could build it in the system.
[47:04] Um, we've we obviously know,
[47:08] you know, we just use ours, but um, you
[47:11] know, you could you could build this in,
[47:13] right? I mean, I'm just trying to make
[47:16] sure that smart like smartly people are
[47:17] the most important. I guess let me ask
[47:19] you this. So, I don't want to I hate to
[47:20] present back the What are your thoughts
[47:22] on this? Like, is this is this something
[47:24] that could be a problem for you today?
[47:25] Like, are you dealing with this today?
[47:27] Do you think you might be off on these?
[47:29] >> I'm pretty new I'm pretty new to this,
[47:30] so I'm exploring all the tools. Um, and
[47:34] you know, I guess what I'm most
[47:36] interested is just finding the best
[47:38] individual vendors. And I kind of get
[47:40] the logic behind Waterfall, but I'm
[47:42] like,
[47:43] >> well, I don't know. I guess that's one
[47:44] option. The other option is just to to
[47:46] patch together a bunch of vendors
[47:47] myself, right? Um, so
[47:49] >> yeah. Yeah.
[47:51] >> Yeah, it's a great question you asked. I
[47:52] mean, you asked a very good question. I
[47:53] don't have a great answer for it right
[47:55] now. I think there's still some stuff
[47:56] being worked out there. I think they are
[47:58] going to add a feature. I've asked them
[48:00] to add it and they're going to add it.
[48:01] There are engineering teams already
[48:02] working on this, so it's going to be
[48:04] done pretty quickly here. um they're
[48:06] going to have a way to check that or uh
[48:08] basically what I think you'll be able to
[48:09] do is flag it where you can click here
[48:13] to my goal would be to get a button that
[48:16] says stop the waterfall if the
[48:18] employment verification goes bad. That
[48:20] would be the goal. Now I know that
[48:23] >> yeah that would be the goal. Now that
[48:25] would unfortunately on that you'd have
[48:27] to trust us blindly. So possibly it
[48:30] might make more sense to put it into
[48:31] another
[48:33] couple tools to like or like you know
[48:36] we're gonna have we'll have an
[48:37] employment verification API as well. So
[48:40] that's something that possibly could
[48:41] happen. Uh I'm just trying to map it in.
[48:43] Obviously I got to worry about like you
[48:45] know cost structure and all that but
[48:46] like we're actually delivering it today.
[48:49] I can't promise it's going to go forever
[48:50] but today it's totally included in the
[48:53] request. A kind of a follow-up question
[48:55] on that is so what percentage of of
[48:58] emails are you say would you say is
[49:00] potentially going to um people who you
[49:05] know it finds a potential email person
[49:07] actually
[49:07] >> there's a lot there's a lot and they're
[49:10] mostly uh yeah there it I'll tell you
[49:13] the answer to that it actually depends
[49:15] on the list you started with
[49:18] >> okay
[49:19] >> so uh I'll tell you where most the flow
[49:22] that I see most agency's doing right
[49:24] now. They're using Apollo,
[49:28] which Apollo gets their data. We don't
[49:32] know, but we're assuming it comes from
[49:33] Sales Navigator
[49:36] uh because or sales like LinkedIn
[49:40] because of because of their uh you know,
[49:43] their company got removed from LinkedIn.
[49:45] So, I'm assuming that's why I we don't
[49:47] know, right? Like we're all this is all
[49:48] speculation. I don't really know like
[49:50] I'm assuming it's it's somewhere there.
[49:51] I mean, the images came from the
[49:53] LinkedIn URL, but we don't really know.
[49:55] And Apollo's good, right? Like, I think
[49:57] they got one of the best like s like
[49:59] their UI is just like brilliant on the
[50:02] like the left sidebar. You know what I'm
[50:03] talking about? Like to to do a search.
[50:06] It's really good. It's like really
[50:08] clean, very easy to use. I really like
[50:09] Apollo's search the best. Like I think
[50:12] it's even better than sales navigator
[50:14] search at some point, but like the data
[50:16] is too close. So, I think LinkedIn
[50:18] wasn't really a fan of that. I'm trying
[50:20] to say this in the right language here,
[50:22] but um that's what happened there. But
[50:24] like if you look, it just depends on
[50:26] where the list came from. So if you
[50:28] start with Zoom Info, who know like I
[50:30] haven't tested, I've been talking to
[50:32] Joey Yilki about this a little bit too,
[50:34] but like testing the actual like list,
[50:37] the list is the strategy. Testing it
[50:40] before you put it into the waterfall or
[50:43] whatever vendors you're using is the
[50:45] biggest critical most point. I haven't
[50:48] done enough testing to say who has the
[50:50] best starting list. Uh it depends on
[50:52] who's closest to the, you know, the
[50:55] closest source is going to be the one
[50:56] that tells you absolutely for no reason
[50:59] and we're not doing it. You would not
[51:00] want to scrape LinkedIn because you'd be
[51:03] violating their terms and addition.
[51:04] However, it's probably the most accurate
[51:06] source
[51:09] if that makes sense.
[51:12] >> It does. It does, Jesse. And one more
[51:14] question from the chat from Brandon. Uh
[51:16] so it's the bottom line that lead magic
[51:18] bulk email verification is the most
[51:20] accurate because you can check current
[51:22] employment and if you mark an email at
[51:24] catch all we should probably not send to
[51:26] it.
[51:29] >> It's a good question. Uh the word
[51:31] accurate would have to be defined.
[51:33] So my opinion is the most and it's hard
[51:36] because I'm very biased because I've
[51:38] created the product. I'm the product
[51:39] manager, right? Like I'm the CTO of the
[51:41] company like CEO, right? Like I I have
[51:44] to take the word accurate and I have to
[51:46] ask there's a few follow-up questions.
[51:48] Would you say that the most
[51:51] accurate means the person works there?
[51:54] Yes. Then I would say yes, we are the
[51:56] most accurate there. Would you say that
[51:58] it's a real inbox? Yes. Then we would be
[52:00] the most accurate there. Would you say
[52:02] that it has a network verification? Yes,
[52:04] it's the most accurate there. So, those
[52:07] things being considered, if we're
[52:08] looking at the clay waterfall, yes,
[52:10] there could be other APIs that I'm not
[52:11] aware of or whatever, then yeah, but I
[52:14] don't know what else we're comparing it
[52:16] to, and I don't I want to define the
[52:17] word accurate because I did talk to um a
[52:20] vendor the other day, and they were in
[52:22] my comments. You can go look at my
[52:23] LinkedIn and see it, but we were in a
[52:24] little bit of an argument about this,
[52:27] and I like this argument. it helps you
[52:28] get a better email address. But they
[52:30] were saying that they would clearly tell
[52:33] you that it's a valid email even if the
[52:36] person didn't work there,
[52:38] >> right?
[52:39] >> And I think that's
[52:41] that's a slippery slope. They're right
[52:44] though. It is a valid email because it
[52:45] could be an inbox. But I'm not going to
[52:47] give you that because or I'm going to
[52:48] try not to. I might do it occasionally.
[52:50] I'm sorry. You know, I'm human here.
[52:52] We're working on a software platform
[52:54] here. But there there are people out
[52:56] there that will tell you that they find
[52:58] it accurate even if the person doesn't
[53:00] work there.
[53:02] You know, I I don't know how you could
[53:04] explain that. I would say that's a lie.
[53:06] I wouldn't go there, but you know, I'm
[53:08] not an agency. I'm I'm biased as hell. I
[53:10] can't answer the question properly
[53:13] to be honest.
[53:13] >> Fair enough. Fair enough.
[53:15] >> It's not fair. I I really don't want to
[53:17] answer the question because I I can't I
[53:19] I'll let Clay answer the question.
[53:21] >> Right. But a follow-up question from
[53:23] Brendan is when this new feature comes
[53:25] out which you mentioned that Clay is
[53:26] going to push out for this, should we
[53:28] rerun a verification list through LM?
[53:32] >> Should we uh what was the last part of
[53:34] that? I'm sorry, I missed nothing.
[53:34] >> We Yeah. So when the feature comes out,
[53:36] should we rerun a verification list
[53:38] through LM?
[53:41] >> Don't use our validation if you use the
[53:43] finder. You don't need to use it. It's
[53:44] the same result.
[53:48] >> Awesome. One more question from Joshua.
[53:51] Can you put a new column check
[53:53] specifically for currently works there
[53:55] or not? If not, don't continue
[53:58] waterfall. Is that currently able to be
[54:00] done or no?
[54:02] >> So again,
[54:04] >> you could do it in clay today. Yes, you
[54:06] could. Yep, you definitely could. Um we
[54:09] give this so this column is here now. Uh
[54:12] unfortunately what you'd have to do is
[54:14] you would have to go and add uh you
[54:19] would have to go off the books. You
[54:21] would have to add our HTTP which uh you
[54:24] would have to do it on your own.
[54:26] >> Right. And this could be done using
[54:31] >> Sorry. Go ahead.
[54:32] >> So the the next point to this was can
[54:34] this be done using lead magic's API
[54:36] inside?
[54:39] >> Yes, that can be done. Yes. on this.
[54:41] >> Yep. So, if you go to our docs page, uh
[54:44] actually there's one update to it, but
[54:45] if you go to the docs page, and I wasn't
[54:47] trying to make this I hope I wasn't, you
[54:48] know, I didn't want to make this like a
[54:50] lead magic infomercial. That's not
[54:51] definitely wasn't what I was designing
[54:52] it to be, but it sounded like that. I
[54:55] wasn't trying. But, you know, I'm just
[54:57] these are just facts, right? But there's
[54:59] other fields that if you do go to the H
[55:02] sheet, if you do go to our our docs, you
[55:04] can see there are other fields we
[55:06] provide which Clay does not have in
[55:08] there for for their um their system.
[55:11] It's because there's other ways to get
[55:13] this in the system. But there are other
[55:15] ways to do it. So if you have an API key
[55:17] through us, you could still use that.
[55:18] You just have to use the HTTP. So you
[55:20] would have to do this, right? You'd have
[55:22] to add HTTP and you'd have to do this
[55:25] command and then you'd have to say
[55:27] employment verification stop the
[55:29] waterfall and do not go on because in
[55:32] this one you don't get anything you
[55:34] don't get anything back
[55:35] >> right
[55:36] >> on this. So you it doesn't check box
[55:39] here, but it it it you you know what I
[55:42] mean? Like it's not you have to be
[55:43] careful here. But I don't know. I mean,
[55:46] I'd like to take even a vote like, you
[55:48] know, if you if you have a way to do a
[55:49] vote, like which which way do people
[55:51] want it? Would you want to email people
[55:53] that work at the company or not? I'm
[55:55] sure there's a varying group of opinions
[55:58] on this. I don't know. I'd love to hear
[55:59] that. Like I I I would want them to work
[56:01] there if I got the email address. That
[56:02] would be my preference, but you know, I
[56:05] can disagree with people too and still
[56:06] like them.
[56:07] >> No, 100%. My personal preference would
[56:09] be
[56:10] >> I love her.
[56:12] >> 100%. Because there are cases, Jesse,
[56:15] where let's say I work for a company, I
[56:17] leave the company, the mailboxes were
[56:19] not removed and technically the email
[56:22] doesn't come to me, right? Or I take
[56:23] some time to delete those mailboxes. So,
[56:25] it isn't really valid. Makes a lot of
[56:27] sense.
[56:29] >> Where did you work before? Akash
[56:32] >> uh I was with uh Clinty. I was with on
[56:36] top.
[56:37] So Clinty is a sales engagement tool. If
[56:39] you know you you do know it.
[56:42] >> Yeah. Yeah. Yeah. Yeah. Yeah. I'm
[56:43] familiar. Yeah. Let's see.
[56:47] Uh
[56:56] >> I feel like a I feel like a laby. I feel
[56:59] like a lab rat. I know.
[57:03] >> Who would get your email now? Would you
[57:05] Is there any chance that they would
[57:06] respond to the email or No,
[57:08] >> no chance. No chance.
[57:13] >> What What actually would be the best I'm
[57:15] going to tell you what I what I'm hoping
[57:16] for in a week. I'm hoping that these
[57:19] tools
[57:20] change because of me on this. I would be
[57:23] so happy if they did. And some of them
[57:25] are going to change, which would make me
[57:27] so happy because I made everybody better
[57:29] by doing this thing.
[57:31] >> That would be my entire goal is to
[57:33] disrupt the whole thing and just make it
[57:35] better for everybody because I think
[57:37] ultimately everybody's going to get
[57:38] better if we all get better. And that's
[57:40] the way I look at life. And I don't
[57:41] there's just no other way to really look
[57:42] at it.
[57:44] >> 100%.
[57:46] >> Yeah. I mean, it looks like even This is
[57:49] interesting. They've I don't think I
[57:51] don't think this is this is an
[57:52] interesting this is this make Oh, I know
[57:54] why. So, sorry. Uh you know what's going
[57:58] on here. So, Clinty is probably not
[58:00] using catchall.
[58:02] >> Ah, right.
[58:04] >> So, this is where this is where the most
[58:07] risk comes in. If they know it's it's a
[58:11] catchall, that's when the that's when
[58:14] you're you're you're I forgot to tell
[58:16] like that's why. So this is the this is
[58:19] the gap that I found right this is the
[58:22] whole like you know and then if you if
[58:26] you have a catchall email address so
[58:29] remember catchall is a domainwide
[58:34] problem or or like status it's not one
[58:37] user on the platform it's everybody on
[58:40] the platform
[58:43] >> 100% makes a lot of sense
[58:45] >> so so they get invalid They might have a
[58:48] check at the very end that says the
[58:50] person doesn't work there anymore.
[58:52] >> True. True.
[58:55] >> At the end of the day,
[58:55] >> also some of these vendors are using us.
[58:58] I' I've actually found some of these
[58:59] vendors are using us for email funding,
[59:02] >> believe it or not, because our costs are
[59:04] so low that they can actually do that.
[59:08] >> But we're like one of the steps.
[59:11] So
[59:13] >> the problem is they still waterfall
[59:14] through to the bad vendor or whatever
[59:17] whatever depending on your opinion of
[59:18] accuracy of what and that's sort of like
[59:21] how it is.
[59:24] >> Well, thank you so much J. I think uh
[59:26] thank you so much for breaking it down
[59:28] here first. Thank you for giving it a
[59:29] smart lead first and I think sessions
[59:31] with you have always been this rather
[59:33] than going over normal deliverability
[59:34] stuff. It's more of uh unlocking a
[59:37] special part of your brain. But thank
[59:38] you for this. Yes, I think no more
[59:39] questions on the chat, but Jesse,
[59:41] anything that you would want to add
[59:42] before we leave, sir?
[59:45] >> Yes, thank you very much. Uh, we are
[59:48] very much happy to work with people.
[59:50] Also, listen, if you find things that we
[59:52] miss, certainly tell us. We we're we're
[59:54] very open to working with people and I'm
[59:56] going to tell you, we are going to miss
[59:58] stuff. Uh, I don't want to guarantee
[01:00:00] anything on that and that would be the
[01:00:01] wrong way to do it. And I also think
[01:00:04] that the value prop of we find more like
[01:00:07] 30% more than every other provider,
[01:00:09] which isn't even true, that value prop
[01:00:12] has just been crushed. I think I just
[01:00:15] crushed that entire story for somebody.
[01:00:17] They're going to have to rewrite their
[01:00:18] playbook. So enjoy rewrite that
[01:00:21] playbook.
[01:00:23] >> Jesse, Jesse, Jesse, thank you so much,
[01:00:26] Jesse. Thank you so much for taking
[01:00:28] >> Thank you so much for bringing it here.
[01:00:30] Thank you all for taking time. And as
[01:00:32] you all know, three consistent things in
[01:00:34] life. Death, taxes, and office hours
[01:00:36] every Thursday. See you all next week.
[01:00:38] See you all tomorrow. Tata. Bye-bye.
[01:00:41] I'll catch you all tomorrow. Yeah.
[01:00:42] Bye-bye.
